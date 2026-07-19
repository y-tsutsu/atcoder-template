import unittest

from tests.string._loader import load_string_module


class TestTrieTree(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.TrieTree = load_string_module('trie_tree')['TrieTree']

    def setUp(self):
        self.trie = self.TrieTree()
        for word in ('abcd', 'abcc', 'abxyz', 'abx', 'abxy', 'b', 'bb', 'bbb', 'ccc'):
            self.trie.insert(word)

    def test_search(self):
        for word in ('abcd', 'abcc', 'abxyz', 'abx', 'abxy', 'b', 'bb', 'bbb', 'ccc'):
            self.assertTrue(self.trie.search(word))
        for word in ('', 'a', 'ab', 'abc', 'abce', 'bbbb', 'z'):
            self.assertFalse(self.trie.search(word))

    def test_prefix(self):
        for prefix in ('', 'a', 'ab', 'abc', 'abx', 'b', 'bb', 'c', 'cc'):
            self.assertTrue(self.trie.prefix_with(prefix))
        for prefix in ('abce', 'bbbb', 'z'):
            self.assertFalse(self.trie.prefix_with(prefix))

    def test_common_prefix(self):
        for prefix in ('', 'a', 'ab', 'abc', 'abx', 'abxy', 'b', 'bb'):
            self.assertTrue(self.trie.common_prefix_with(prefix))
        for prefix in ('abcd', 'abxyz', 'bbb', 'c', 'cc', 'ccc', 'z'):
            self.assertFalse(self.trie.common_prefix_with(prefix))

    def test_lcp(self):
        expected = {
            'abcd': 'abc',
            'abcc': 'abc',
            'abxyz': 'abxy',
            'abx': 'abx',
            'bbb': 'bb',
            'ccc': '',
            'abcz': 'abc',
            'z': '',
        }
        for text, lcp in expected.items():
            self.assertEqual(self.trie.lcp(text), lcp)

    def test_duplicate_and_empty_string(self):
        self.trie.insert('abx')
        self.trie.insert('')
        self.assertTrue(self.trie.search(''))
        self.assertEqual(self.trie._root.count, 11)
        self.assertEqual(self.trie._root.children['a'].children['b'].children['x'].count, 4)

    def test_dfs(self):
        self.assertIsNone(self.trie.dfs())


if __name__ == '__main__':
    unittest.main()
