from bisect import bisect_left, insort
from random import Random
import unittest

from data_structures.binary_trie import BinaryTrie


class TestBinaryTrie(unittest.TestCase):
    def test_basic_operations(self):
        trie = BinaryTrie(max_bit=3)
        for x in (1, 3, 3, 8, 10):
            trie.insert(x)
        self.assertEqual(len(trie), 5)
        self.assertEqual(trie.count(3), 2)
        self.assertEqual([trie.kth(i) for i in range(len(trie))], [1, 3, 3, 8, 10])
        self.assertEqual(trie.count_less(8), 3)
        self.assertTrue(trie.erase(3))
        self.assertEqual(trie.count(3), 1)
        self.assertFalse(trie.erase(7))

    def test_xor_queries(self):
        trie = BinaryTrie(max_bit=3)
        values = [1, 3, 3, 8, 10]
        for x in values:
            trie.insert(x)
        for x in range(16):
            self.assertEqual(trie.min_xor(x), min(x ^ y for y in values))
            self.assertEqual(trie.max_xor(x), max(x ^ y for y in values))
            self.assertEqual(x ^ trie.argmin_xor(x), trie.min_xor(x))
            self.assertEqual(x ^ trie.argmax_xor(x), trie.max_xor(x))

    def test_matches_sorted_list(self):
        rng = Random(0)
        trie = BinaryTrie(max_bit=7)
        values = []
        for _ in range(500):
            x = rng.randrange(256)
            if not values or rng.randrange(2) == 0:
                trie.insert(x)
                insort(values, x)
            else:
                expected = x in values
                self.assertEqual(trie.erase(x), expected)
                if expected:
                    values.remove(x)

            self.assertEqual(len(trie), len(values))
            self.assertEqual(trie.count(x), values.count(x))
            for y in (0, 1, 64, 128, 255, 256):
                self.assertEqual(trie.count_less(y), bisect_left(values, y))
            if values:
                k = rng.randrange(len(values))
                self.assertEqual(trie.kth(k), values[k])
                self.assertEqual(trie.min_xor(x), min(x ^ y for y in values))
                self.assertEqual(trie.max_xor(x), max(x ^ y for y in values))

    def test_boundaries(self):
        trie = BinaryTrie(max_bit=2)
        with self.assertRaises(AssertionError):
            trie.insert(-1)
        with self.assertRaises(AssertionError):
            trie.insert(8)
        with self.assertRaises(AssertionError):
            trie.kth(0)
        with self.assertRaises(AssertionError):
            trie.min_xor(0)


if __name__ == '__main__':
    unittest.main()
