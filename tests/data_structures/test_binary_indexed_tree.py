import unittest

from algorithms.bisect_lambda import bisect_ng_ok
from data_structures import binary_indexed_tree
from data_structures.binary_indexed_tree import BIT
from data_structures.binary_indexed_tree import BITAddRange
from data_structures.binary_indexed_tree import BITSortedMultiset


class TestBinaryIndexedTree(unittest.TestCase):
    def test_bit(self):
        bit = BIT(5)
        for i, x in enumerate([3, 1, 4, 1, 5]):
            bit.add(i, x)
        self.assertEqual(bit.sum(1, 4), 6)
        self.assertEqual(bit.get(2), 4)
        bit.set(2, 9)
        self.assertEqual(bit.sum(0, 5), 19)

    def test_add_range(self):
        bit = BITAddRange(5)
        bit.add(1, 4, 2)
        bit.add(2, 5, 3)
        self.assertEqual([bit.get(i) for i in range(5)], [0, 2, 5, 5, 3])

    def test_sorted_multiset(self):
        binary_indexed_tree.bisect_ng_ok = bisect_ng_ok
        multiset = BITSortedMultiset(5)
        for x in [3, 1, 3, 5]:
            multiset.add(x)
        self.assertEqual(str(multiset), '[1, 3, 3, 5]')
        self.assertEqual([multiset[i] for i in range(4)], [1, 3, 3, 5])
        multiset.discard(3)
        self.assertEqual(str(multiset), '[1, 3, 5]')

    def test_sorted_multiset_rejects_negative_value(self):
        multiset = BITSortedMultiset(5)
        with self.assertRaises(AssertionError):
            multiset.add(-1)
        with self.assertRaises(AssertionError):
            -1 in multiset
        with self.assertRaises(AssertionError):
            multiset.discard(-1)


if __name__ == '__main__':
    unittest.main()
