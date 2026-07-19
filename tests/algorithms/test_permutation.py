import unittest

from algorithms.permutation import next_permutation
from algorithms.permutation import prev_permutation


class TestPermutation(unittest.TestCase):
    def test_next_permutation(self):
        a = [1, 2, 3]
        self.assertEqual(next_permutation(a), [1, 3, 2])
        self.assertEqual(a, [1, 2, 3])
        self.assertEqual(next_permutation([1, 1, 2]), [1, 2, 1])
        self.assertIsNone(next_permutation([3, 2, 1]))

    def test_prev_permutation(self):
        a = [3, 2, 1]
        self.assertEqual(prev_permutation(a), [3, 1, 2])
        self.assertEqual(a, [3, 2, 1])
        self.assertEqual(prev_permutation([2, 1, 1]), [1, 2, 1])
        self.assertIsNone(prev_permutation([1, 2, 3]))

    def test_subrange(self):
        self.assertEqual(next_permutation([9, 1, 2, 3, 8], 1, 4), [9, 1, 3, 2, 8])
        self.assertEqual(prev_permutation([9, 3, 2, 1, 8], 1, 4), [9, 3, 1, 2, 8])

    def test_short_sequence(self):
        self.assertIsNone(next_permutation([]))
        self.assertIsNone(next_permutation([1]))
        self.assertIsNone(prev_permutation([]))
        self.assertIsNone(prev_permutation([1]))


if __name__ == '__main__':
    unittest.main()
