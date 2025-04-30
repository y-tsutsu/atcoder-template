def recurboost(func=None, stack=[]):
    pass


class TrieTree:
    class Node:
        def __init__(self, char='', rank=-1, parent=None):
            self.char = char
            self.rank = rank
            self.parent = parent
            self.children = {}
            self.count = 0
            self.value = None

        def is_terminate(self):
            return self.value is not None

    def __init__(self):
        self._root = TrieTree.Node()

    @recurboost
    def insert(self, text, parent=None, pos=0):
        if parent is None:
            parent = self._root
        if pos == len(text):
            parent.value = text
            parent.count += 1
            yield parent
        parent.count += 1
        c = text[pos]
        if c not in parent.children:
            parent.children[c] = TrieTree.Node(char=c, rank=pos, parent=parent)
        node = parent.children[c]
        ret = yield self.insert(text, node, pos + 1)
        yield ret

    @recurboost
    def lcp(self, text, parent=None, pos=0):
        '''最長共通prefix'''
        if parent is None:
            parent = self._root
        if pos == len(text):
            yield text[:parent.rank + 1]
        c = text[pos]
        if c not in parent.children:
            yield text[:parent.rank + 1]
        child = parent.children[c]
        if child.count == 1:
            yield text[:parent.rank + 1]
        ret = yield self.lcp(text, parent.children[c], pos + 1)
        yield ret

    def search(self, text, parent=None, pos=0):
        '''textが登録済みか？'''
        return self._inner_search(text, parent, pos, lambda p: p.is_terminate())

    def prefix_with(self, text, parent=None, pos=0):
        '''textが登録された文字列のprefixとして存在するか？'''
        return self._inner_search(text, parent, pos, lambda _: True)

    def common_prefix_with(self, text, parent=None, pos=0):
        '''textが登録された文字列のうち複数の共通prefixとして存在するか？'''
        return self._inner_search(text, parent, pos, lambda p: p.count >= 2)

    @recurboost
    def _inner_search(self, text, parent, pos, result_funk):
        if parent is None:
            parent = self._root
        if pos == len(text):
            yield result_funk(parent)
        c = text[pos]
        if c not in parent.children:
            yield False
        ret = yield self._inner_search(text, parent.children[c], pos + 1, result_funk)
        yield ret


def example():
    tr = TrieTree()
    tr.insert('abcd')
    tr.insert('abcc')
    tr.insert('abxyz')
    tr.insert('abx')
    tr.insert('abxy')
    tr.insert('b')
    tr.insert('bb')
    tr.insert('bbb')
    tr.insert('ccc')
    print('## count: ##')
    print(tr._root.count == 9)
    print(tr._root.children['a'].count == 5)
    print(tr._root.children['a'].children['b'].count == 5)
    print(tr._root.children['a'].children['b'].children['c'].count == 2)
    print(tr._root.children['a'].children['b'].children['x'].count == 3)
    print(tr._root.children['a'].children['b'].children['c'].children['d'].count == 1)
    print(tr._root.children['a'].children['b'].children['c'].children['c'].count == 1)
    print(tr._root.children['a'].children['b'].children['x'].children['y'].count == 2)
    print(tr._root.children['a'].children['b'].children['x'].children['y'].children['z'].count == 1)
    print(tr._root.children['b'].count == 3)
    print(tr._root.children['b'].children['b'].count == 2)
    print(tr._root.children['b'].children['b'].children['b'].count == 1)
    print(tr._root.children['c'].count == 1)
    print(tr._root.children['c'].children['c'].count == 1)
    print(tr._root.children['c'].children['c'].children['c'].count == 1)
    print(f'## search: {True} ##')
    print(tr.search('abcd'))
    print(tr.search('abcc'))
    print(tr.search('abxyz'))
    print(tr.search('abx'))
    print(tr.search('abxy'))
    print(tr.search('b'))
    print(tr.search('bb'))
    print(tr.search('bbb'))
    print(tr.search('ccc'))
    print(f'## search: {False} ##')
    print(tr.search('a'))
    print(tr.search('ab'))
    print(tr.search('abc'))
    print(tr.search('abce'))
    print(tr.search('abcde'))
    print(tr.search('d'))
    print(tr.search('dd'))
    print(tr.search('ddd'))
    print(tr.search('cc'))
    print(tr.search('c'))
    print(tr.search(''))
    print(f'## prefix_with: {True} ##')
    print(tr.prefix_with('abc'))
    print(tr.prefix_with('ab'))
    print(tr.prefix_with('a'))
    print(tr.prefix_with('abxy'))
    print(tr.prefix_with('abx'))
    print(tr.prefix_with('bb'))
    print(tr.prefix_with('b'))
    print(tr.prefix_with('cc'))
    print(tr.prefix_with('c'))
    print(tr.prefix_with(''))
    print(tr.prefix_with('abcd'))
    print(tr.prefix_with('abcc'))
    print(tr.prefix_with('abxyz'))
    print(tr.prefix_with('bbb'))
    print(tr.prefix_with('ccc'))
    print(f'## prefix_with: {False} ##')
    print(tr.prefix_with('bbbb'))
    print(tr.prefix_with('z'))
    print(f'## common_prefix_with: {True} ##')
    print(tr.common_prefix_with('abc'))
    print(tr.common_prefix_with('ab'))
    print(tr.common_prefix_with('a'))
    print(tr.common_prefix_with('abxy'))
    print(tr.common_prefix_with('abx'))
    print(tr.common_prefix_with('bb'))
    print(tr.common_prefix_with('b'))
    print(tr.common_prefix_with(''))
    print(f'## common_prefix_with: {False} ##')
    print(tr.common_prefix_with('abcd'))
    print(tr.common_prefix_with('abcc'))
    print(tr.common_prefix_with('abxyz'))
    print(tr.common_prefix_with('bbbb'))
    print(tr.common_prefix_with('bbb'))
    print(tr.common_prefix_with('ccc'))
    print(tr.common_prefix_with('cc'))
    print(tr.common_prefix_with('c'))
    print(tr.common_prefix_with('z'))
    print(f'## common_prefix: {True} ##')
    print(tr.lcp('abcd') == 'abc')
    print(tr.lcp('abcc') == 'abc')
    print(tr.lcp('abxyz') == 'abxy')
    print(tr.lcp('abx') == 'abx')
    print(tr.lcp('abxy') == 'abxy')
    print(tr.lcp('b') == 'b')
    print(tr.lcp('bb') == 'bb')
    print(tr.lcp('bbb') == 'bb')
    print(tr.lcp('ccc') == '')
    print(tr.lcp('abcz') == 'abc')
    print(tr.lcp('az') == 'a')
    print(tr.lcp('z') == '')


if __name__ == '__main__':
    example()
