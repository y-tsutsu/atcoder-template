class BinaryTrie:
    '''非負整数をbit列として管理し、順序・XORクエリを行うBinary Trie'''

    class Node:
        __slots__ = ('children', 'count', 'terminal_count')

        def __init__(self):
            self.children = [None, None]
            self.count = 0
            self.terminal_count = 0

    def __init__(self, max_bit=60):
        self._max_bit = max_bit
        self._limit = 1 << (max_bit + 1)
        self._root = BinaryTrie.Node()

    def __len__(self):
        '''重複を含む登録整数数を返す'''
        return self._root.count

    def insert(self, x):
        '''非負整数xを1個登録する'''
        self._assert_value(x)
        node = self._root
        node.count += 1
        for bit in range(self._max_bit, -1, -1):
            b = x >> bit & 1
            if node.children[b] is None:
                node.children[b] = BinaryTrie.Node()
            node = node.children[b]
            node.count += 1
        node.terminal_count += 1

    def erase(self, x):
        '''登録されたxを1個削除し、削除できたかを返す'''
        self._assert_value(x)
        if self.count(x) == 0:
            return False

        node = self._root
        path = []
        node.count -= 1
        for bit in range(self._max_bit, -1, -1):
            b = x >> bit & 1
            path.append((node, b))
            node = node.children[b]
            node.count -= 1
        node.terminal_count -= 1

        for parent, b in reversed(path):
            if parent.children[b].count > 0:
                break
            parent.children[b] = None
        return True

    def count(self, x):
        '''xの登録数を返す'''
        self._assert_value(x)
        node = self._root
        for bit in range(self._max_bit, -1, -1):
            node = node.children[x >> bit & 1]
            if node is None:
                return 0
        return node.terminal_count

    def kth(self, k):
        '''重複込みの昇順で0-indexedのk番目の整数を返す'''
        assert 0 <= k < len(self)
        node = self._root
        ret = 0
        for bit in range(self._max_bit, -1, -1):
            left = node.children[0]
            left_count = 0 if left is None else left.count
            if k < left_count:
                node = left
            else:
                k -= left_count
                node = node.children[1]
                ret |= 1 << bit
        return ret

    def count_less(self, x):
        '''xより小さい登録整数数を返す'''
        if x <= 0:
            return 0
        if x >= self._limit:
            return len(self)
        node = self._root
        ret = 0
        for bit in range(self._max_bit, -1, -1):
            if node is None:
                break
            b = x >> bit & 1
            if b == 1:
                left = node.children[0]
                if left is not None:
                    ret += left.count
            node = node.children[b]
        return ret

    def argmin_xor(self, x):
        '''xとのXORが最小になる登録整数を返す'''
        return self._xor_partner(x, False)

    def argmax_xor(self, x):
        '''xとのXORが最大になる登録整数を返す'''
        return self._xor_partner(x, True)

    def min_xor(self, x):
        '''登録整数とのXORの最小値を返す'''
        return x ^ self.argmin_xor(x)

    def max_xor(self, x):
        '''登録整数とのXORの最大値を返す'''
        return x ^ self.argmax_xor(x)

    def _xor_partner(self, x, maximize):
        self._assert_value(x)
        assert len(self) > 0
        node = self._root
        ret = 0
        for bit in range(self._max_bit, -1, -1):
            b = x >> bit & 1
            preferred = b ^ maximize
            if node.children[preferred] is None:
                preferred ^= 1
            node = node.children[preferred]
            ret |= preferred << bit
        return ret

    def _assert_value(self, x):
        assert 0 <= x < self._limit


def example():
    trie = BinaryTrie(max_bit=3)  # 0以上16未満を管理
    for x in (1, 3, 3, 8, 10):
        trie.insert(x)

    print(len(trie))          # 5: 重複を含む
    print(trie.count(3))      # 2
    print(trie.kth(2))        # 3: [1, 3, 3, 8, 10]の2番目
    print(trie.count_less(8))  # 3

    # 6 XOR 3 = 5が最小、6 XOR 8 = 14が最大
    print(trie.argmin_xor(6))  # 3
    print(trie.min_xor(6))    # 5
    print(trie.argmax_xor(6))  # 8
    print(trie.max_xor(6))    # 14

    trie.erase(3)
    print(trie.count(3))      # 1


if __name__ == '__main__':
    example()
