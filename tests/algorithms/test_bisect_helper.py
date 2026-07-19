import random
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

    def test_matches_naive_search(self):
        random.seed(0)
        for _ in range(100):
            a = sorted(random.randrange(-10, 11) for _ in range(30))
            x = random.randrange(-12, 13)
            less = [v for v in a if v < x]
            less_equal = [v for v in a if v <= x]
            greater = [v for v in a if v > x]
            greater_equal = [v for v in a if v >= x]

            self.assertEqual(lt(a, x), less[-1] if less else None)
            self.assertEqual(le(a, x), less_equal[-1] if less_equal else None)
            self.assertEqual(gt(a, x), greater[0] if greater else None)
            self.assertEqual(ge(a, x), greater_equal[0] if greater_equal else None)
            self.assertEqual(lt_count(a, x), len(less))
            self.assertEqual(le_count(a, x), len(less_equal))
            self.assertEqual(gt_count(a, x), len(greater))
            self.assertEqual(ge_count(a, x), len(greater_equal))

            for k in range(3):
                self.assertEqual(kth_lt(a, x, k), less[-1 - k] if len(less) > k else None)
                self.assertEqual(kth_le(a, x, k), less_equal[-1 - k] if len(less_equal) > k else None)
                self.assertEqual(kth_gt(a, x, k), greater[k] if len(greater) > k else None)
                self.assertEqual(kth_ge(a, x, k), greater_equal[k] if len(greater_equal) > k else None)

    def test_range_count_matches_naive_count(self):
        random.seed(1)
        for _ in range(100):
            a = sorted(random.randrange(-10, 11) for _ in range(30))
            lo = random.randrange(-12, 13)
            hi = random.randrange(lo, 13)
            self.assertEqual(range_inclusive_count(a, lo, hi), sum(lo <= v <= hi for v in a))
            self.assertEqual(range_exclusive_count(a, lo, hi), sum(lo <= v < hi for v in a))


if __name__ == '__main__':
    unittest.main()
