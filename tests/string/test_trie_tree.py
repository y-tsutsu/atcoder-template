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
        self.assertEqual(len(self.trie), 11)
        self.assertEqual(self.trie.distinct_size(), 10)
        self.assertEqual(self.trie.count('abx'), 2)
        self.assertEqual(self.trie._root.prefix_count, 11)
        self.assertEqual(self.trie.count_prefix('abx'), 4)

    def test_erase(self):
        self.trie.insert('abx')
        self.assertTrue(self.trie.erase('abx'))
        self.assertEqual(self.trie.count('abx'), 1)
        self.assertTrue(self.trie.erase('abx'))
        self.assertFalse(self.trie.search('abx'))
        self.assertTrue(self.trie.search('abxy'))
        self.assertFalse(self.trie.erase('abx'))
        self.assertFalse(self.trie.erase('unknown'))

    def test_registered_prefixes(self):
        self.trie.insert('')
        self.assertEqual(
            self.trie.prefixes('abcdx'),
            [('', 1), ('abcd', 1)],
        )
        self.assertEqual(self.trie.longest_prefix('abcdx'), 'abcd')
        self.assertEqual(self.trie.longest_prefix('unknown'), '')

    def test_items_and_words(self):
        self.trie.insert('abx')
        self.assertEqual(
            self.trie.items('abx'),
            [('abx', 2), ('abxy', 1), ('abxyz', 1)],
        )
        self.assertEqual(
            self.trie.words('abx'),
            ['abx', 'abx', 'abxy', 'abxyz'],
        )
        self.assertEqual(self.trie.items('unknown'), [])

    def test_kth(self):
        self.trie.insert('abx')
        words = self.trie.words()
        self.assertEqual([self.trie.kth(i) for i in range(len(self.trie))], words)
        with self.assertRaises(AssertionError):
            self.trie.kth(-1)
        with self.assertRaises(AssertionError):
            self.trie.kth(len(self.trie))

    def test_bisect(self):
        self.trie.insert('abx')
        words = self.trie.words()
        for text in ('', 'a', 'abx', 'abxx', 'b', 'bc', 'z'):
            expected_left = sum(word < text for word in words)
            expected_right = sum(word <= text for word in words)
            self.assertEqual(self.trie.bisect_left(text), expected_left)
            self.assertEqual(self.trie.bisect_right(text), expected_right)

    def test_prev_and_next(self):
        self.trie.insert('abx')
        self.assertEqual(self.trie.prev('abx'), 'abcd')
        self.assertEqual(self.trie.next('abx'), 'abxy')
        self.assertEqual(self.trie.prev('abxx'), 'abx')
        self.assertEqual(self.trie.next('abxx'), 'abxy')
        self.assertIsNone(self.trie.prev(''))
        self.assertIsNone(self.trie.next('z'))


if __name__ == '__main__':
    unittest.main()
