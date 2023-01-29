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

        def __eq__(self, other):
            if not isinstance(other, TrieTree.Node):
                return False
            return self.char == other.char

        def __hash__(self):
            return hash(self.char)

        def __str__(self):
            return f'{self.char} {self.rank} {self.count} {self.value}'

    def __init__(self):
        self._root = TrieTree.Node()

    def insert(self, text, parent=None, pos=0):
        if parent is None:
            parent = self._root
        if pos == len(text):
            parent.value = text
            parent.count += 1
            return
        parent.count += 1
        c = text[pos]
        if c not in parent.children:
            parent.children[c] = TrieTree.Node(char=c, rank=pos, parent=parent)
        node = parent.children[c]
        self.insert(text, node, pos + 1)

    def search(self, text, parent=None, pos=0):
        return self._inner_search(text, parent, pos, lambda p: p.is_terminate())

    def prefix_with(self, text, parent=None, pos=0):
        return self._inner_search(text, parent, pos, lambda p: True)

    def common_prefix_with(self, text, parent=None, pos=0):
        return self._inner_search(text, parent, pos, lambda p: (p.is_terminate() and p.count >= 2) or (not p.is_terminate() and p.count >= 2))

    def _inner_search(self, text, parent, pos, result_funk):
        if parent is None:
            parent = self._root
        if pos == len(text):
            return result_funk(parent)
        c = text[pos]
        if c not in parent.children:
            return False
        return self._inner_search(text, parent.children[c], pos + 1, result_funk)

    def common_prefix(self, text, parent=None, pos=0):
        if parent is None:
            parent = self._root
        if pos == len(text):
            return text[:parent.rank + 1]
        c = text[pos]
        if c not in parent.children:
            return text[:parent.rank + 1]
        child = parent.children[c]
        if child.count == 1:
            return text[:parent.rank + 1]
        return self.common_prefix(text, parent.children[c], pos + 1)


def main():
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
    print('// count: //')
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
    print(f'// search: {True} //')
    print(tr.search('abcd'))
    print(tr.search('abcc'))
    print(tr.search('abxyz'))
    print(tr.search('abx'))
    print(tr.search('abxy'))
    print(tr.search('b'))
    print(tr.search('bb'))
    print(tr.search('bbb'))
    print(tr.search('ccc'))
    print(f'// search: {False} //')
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
    print(f'// prefix_with: {True} //')
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
    print(f'// prefix_with: {False} //')
    print(tr.prefix_with('bbbb'))
    print(tr.prefix_with('z'))
    print(f'// common_prefix_with: {True} //')
    print(tr.common_prefix_with('abc'))
    print(tr.common_prefix_with('ab'))
    print(tr.common_prefix_with('a'))
    print(tr.common_prefix_with('abxy'))
    print(tr.common_prefix_with('abx'))
    print(tr.common_prefix_with('bb'))
    print(tr.common_prefix_with('b'))
    print(tr.common_prefix_with(''))
    print(f'// common_prefix_with: {False} //')
    print(tr.common_prefix_with('abcd'))
    print(tr.common_prefix_with('abcc'))
    print(tr.common_prefix_with('abxyz'))
    print(tr.common_prefix_with('bbbb'))
    print(tr.common_prefix_with('bbb'))
    print(tr.common_prefix_with('ccc'))
    print(tr.common_prefix_with('cc'))
    print(tr.common_prefix_with('c'))
    print(tr.common_prefix_with('z'))
    print(f'// common_prefix: {True} //')
    print(tr.common_prefix('abcd') == 'abc')
    print(tr.common_prefix('abcc') == 'abc')
    print(tr.common_prefix('abxyz') == 'abxy')
    print(tr.common_prefix('abx') == 'abx')
    print(tr.common_prefix('abxy') == 'abxy')
    print(tr.common_prefix('b') == 'b')
    print(tr.common_prefix('bb') == 'bb')
    print(tr.common_prefix('bbb') == 'bb')
    print(tr.common_prefix('ccc') == '')
    print(tr.common_prefix('abcz') == 'abc')
    print(tr.common_prefix('az') == 'a')
    print(tr.common_prefix('z') == '')


if __name__ == '__main__':
    main()
