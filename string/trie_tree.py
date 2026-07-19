class TrieTree:
    '''文字列の検索・prefix検索・辞書順操作を文字列長に比例する時間で行うTrie木'''

    class Node:
        __slots__ = ('children', 'prefix_count', 'terminal_count')

        def __init__(self):
            self.children = {}
            self.prefix_count = 0
            self.terminal_count = 0

    def __init__(self):
        self._root = TrieTree.Node()
        self._distinct_size = 0

    def __len__(self):
        '''重複を含む登録文字列数を返す'''
        return self._root.prefix_count

    def insert(self, text):
        '''文字列を1個登録し、終端ノードを返す'''
        node = self._root
        node.prefix_count += 1
        for c in text:
            if c not in node.children:
                node.children[c] = TrieTree.Node()
            node = node.children[c]
            node.prefix_count += 1
        if node.terminal_count == 0:
            self._distinct_size += 1
        node.terminal_count += 1
        return node

    def erase(self, text):
        '''登録された文字列を1個削除し、削除できたかを返す'''
        node = self._root
        path = [node]
        for c in text:
            if c not in node.children:
                return False
            node = node.children[c]
            path.append(node)
        if node.terminal_count == 0:
            return False

        node.terminal_count -= 1
        if node.terminal_count == 0:
            self._distinct_size -= 1
        for node in path:
            node.prefix_count -= 1
        for i in range(len(text) - 1, -1, -1):
            parent = path[i]
            child = path[i + 1]
            if child.prefix_count > 0:
                break
            del parent.children[text[i]]
        return True

    def count(self, text):
        '''文字列の登録数を返す'''
        node = self._find_node(text)
        return 0 if node is None else node.terminal_count

    def count_prefix(self, prefix):
        '''prefixで始まる登録文字列数を返す'''
        node = self._find_node(prefix)
        return 0 if node is None else node.prefix_count

    def distinct_size(self):
        '''重複を除いた登録文字列数を返す'''
        return self._distinct_size

    def search(self, text):
        '''文字列が1個以上登録されているかを返す'''
        return self.count(text) > 0

    def prefix_with(self, prefix):
        '''prefixで始まる登録文字列が存在するかを返す'''
        return self.count_prefix(prefix) > 0

    def common_prefix_with(self, prefix):
        '''prefixで始まる登録文字列が2個以上存在するかを返す'''
        return self.count_prefix(prefix) >= 2

    def prefixes(self, text):
        '''textのprefixとして登録されている文字列と登録数を短い順に返す'''
        ret = []
        node = self._root
        if node.terminal_count > 0:
            ret.append(('', node.terminal_count))
        for i, c in enumerate(text):
            if c not in node.children:
                break
            node = node.children[c]
            if node.terminal_count > 0:
                ret.append((text[:i + 1], node.terminal_count))
        return ret

    def longest_prefix(self, text):
        '''textのprefixとして登録されている最長の文字列を返す'''
        node = self._root
        length = 0 if node.terminal_count > 0 else -1
        for i, c in enumerate(text):
            if c not in node.children:
                break
            node = node.children[c]
            if node.terminal_count > 0:
                length = i + 1
        return None if length < 0 else text[:length]

    def lcp(self, text):
        '''textのうち2個以上の登録文字列が共有する最長prefixを返す'''
        node = self._root
        i = 0
        while i < len(text):
            c = text[i]
            if c not in node.children:
                break
            child = node.children[c]
            if child.prefix_count < 2:
                break
            node = child
            i += 1
        return text[:i]

    def items(self, prefix=''):
        '''prefixで始まる登録文字列と登録数を辞書順に返す'''
        node = self._find_node(prefix)
        if node is None:
            return []
        ret = []
        stack = [(node, prefix)]
        while stack:
            node, text = stack.pop()
            if node.terminal_count > 0:
                ret.append((text, node.terminal_count))
            for c, child in sorted(node.children.items(), reverse=True):
                stack.append((child, text + c))
        return ret

    def words(self, prefix=''):
        '''prefixで始まる登録文字列を重複込みの辞書順で返す'''
        return [text for text, count in self.items(prefix) for _ in range(count)]

    def kth(self, k):
        '''重複込みの辞書順で0-indexedのk番目の文字列を返す'''
        assert 0 <= k < len(self)
        node = self._root
        text = ''
        while True:
            if k < node.terminal_count:
                return text
            k -= node.terminal_count
            for c, child in sorted(node.children.items()):
                if k < child.prefix_count:
                    node = child
                    text += c
                    break
                k -= child.prefix_count

    def bisect_left(self, text):
        '''textより辞書順で小さい登録文字列数を返す'''
        node = self._root
        ret = 0
        for c in text:
            ret += node.terminal_count
            for key, child in node.children.items():
                if key < c:
                    ret += child.prefix_count
            if c not in node.children:
                return ret
            node = node.children[c]
        return ret

    def bisect_right(self, text):
        '''text以下の登録文字列数を返す'''
        return self.bisect_left(text) + self.count(text)

    def prev(self, text):
        '''textより辞書順で小さい最大の登録文字列を返す'''
        i = self.bisect_left(text)
        return None if i == 0 else self.kth(i - 1)

    def next(self, text):
        '''textより辞書順で大きい最小の登録文字列を返す'''
        i = self.bisect_right(text)
        return None if i == len(self) else self.kth(i)

    def _find_node(self, text):
        node = self._root
        for c in text:
            if c not in node.children:
                return None
            node = node.children[c]
        return node


def example():
    trie = TrieTree()
    for word in ('app', 'apple', 'apple', 'apply', 'bat'):
        trie.insert(word)

    # 完全一致の検索と登録数
    print(trie.search('apple'))       # True
    print(trie.search('ap'))          # False
    print(trie.count('apple'))        # 2

    # prefix検索と、そのprefixを持つ文字列数
    print(trie.prefix_with('app'))     # True
    print(trie.count_prefix('app'))    # 4
    print(trie.count_prefix('cat'))    # 0

    # 入力文字列のprefixとして登録済みの文字列を探す
    print(trie.prefixes('applepie'))   # [('app', 1), ('apple', 2)]
    print(trie.longest_prefix('apply'))  # apply

    # 辞書順列挙とk番目の文字列（重複を含む）
    print(trie.items('app'))           # [('app', 1), ('apple', 2), ('apply', 1)]
    print(trie.words())                # app, apple, apple, apply, bat
    print(trie.kth(3))                 # apply

    # 登録されていない文字列に対しても辞書順の前後を探せる
    print(trie.prev('ball'))            # apply
    print(trie.next('ball'))            # bat

    # 1個ずつ削除でき、登録数が0になると検索にもヒットしなくなる
    trie.erase('apple')
    print(trie.count('apple'))         # 1


if __name__ == '__main__':
    example()
