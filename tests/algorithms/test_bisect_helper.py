import unittest

from algorithms.bisect_helper import ge
from algorithms.bisect_helper import ge_count
from algorithms.bisect_helper import gt
from algorithms.bisect_helper import gt_count
from algorithms.bisect_helper import kth_ge
from algorithms.bisect_helper import kth_gt
from algorithms.bisect_helper import kth_le
from algorithms.bisect_helper import kth_lt
from algorithms.bisect_helper import le
from algorithms.bisect_helper import le_count
from algorithms.bisect_helper import lt
from algorithms.bisect_helper import lt_count
from algorithms.bisect_helper import range_exclusive_count
from algorithms.bisect_helper import range_inclusive_count


class TestBisectHelper(unittest.TestCase):
    def setUp(self):
        self.a = [1, 2, 2, 4, 7]

    def test_find_neighbor(self):
        self.assertEqual(lt(self.a, 2), 1)
        self.assertEqual(le(self.a, 2), 2)
        self.assertEqual(gt(self.a, 2), 4)
        self.assertEqual(ge(self.a, 2), 2)

    def test_find_neighbor_returns_none(self):
        self.assertIsNone(lt(self.a, 1))
        self.assertIsNone(le(self.a, 0))
        self.assertIsNone(gt(self.a, 7))
        self.assertIsNone(ge(self.a, 8))

    def test_count(self):
        self.assertEqual(lt_count(self.a, 2), 1)
        self.assertEqual(le_count(self.a, 2), 3)
        self.assertEqual(gt_count(self.a, 2), 2)
        self.assertEqual(ge_count(self.a, 2), 4)
        self.assertEqual(range_inclusive_count(self.a, 2, 4), 3)
        self.assertEqual(range_exclusive_count(self.a, 2, 4), 2)

    def test_kth_neighbor(self):
        self.assertEqual(kth_lt(self.a, 7, 1), 2)
        self.assertEqual(kth_le(self.a, 2, 1), 2)
        self.assertEqual(kth_gt(self.a, 2, 1), 7)
        self.assertEqual(kth_ge(self.a, 2, 2), 4)
        self.assertIsNone(kth_lt(self.a, 1))
        self.assertIsNone(kth_gt(self.a, 7))

    def test_empty(self):
        self.assertIsNone(lt([], 1))
        self.assertIsNone(le([], 1))
        self.assertIsNone(gt([], 1))
        self.assertIsNone(ge([], 1))


if __name__ == '__main__':
    unittest.main()
