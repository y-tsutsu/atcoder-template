from math import gcd
import unittest

from data_structures.sparse_table import SparseTable


class TestSparseTable(unittest.TestCase):
    def test_min_max_and_gcd(self):
        a = [12, 18, 6, 15, 9, 21]
        for op in (min, max, gcd):
            sparse_table = SparseTable(a, op)
            self.assertEqual(len(sparse_table), len(a))
            for s in range(len(a)):
                expected = a[s]
                for e in range(s + 1, len(a) + 1):
                    expected = op(expected, a[e - 1])
                    self.assertEqual(sparse_table.prod(s, e), expected)

    def test_single_element(self):
        sparse_table = SparseTable([42], min)
        self.assertEqual(sparse_table.prod(0, 1), 42)

    def test_rejects_empty_array_and_empty_range(self):
        with self.assertRaises(AssertionError):
            SparseTable([], min)
        with self.assertRaises(AssertionError):
            SparseTable([1, 2, 3], min).prod(1, 1)


if __name__ == '__main__':
    unittest.main()
