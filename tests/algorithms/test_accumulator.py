import unittest

from algorithms.accumulator import acm2dim_helper
from algorithms.accumulator import acm3dim_helper
from algorithms.accumulator import acm_helper
from algorithms.accumulator import accumulate2dim
from algorithms.accumulator import accumulate3dim
from algorithms.accumulator import imos2d_helper
from algorithms.accumulator import imos3d_helper
from algorithms.accumulator import imos_helper


class TestAccumulator(unittest.TestCase):
    def test_range_sum(self):
        range_sum = acm_helper([1, 2, 3, 4])
        self.assertEqual(range_sum(1, 3), 5)
        self.assertEqual(range_sum(2, 2), 0)

    def test_prefix_sum_2d(self):
        a = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(accumulate2dim(a), [[0, 0, 0, 0], [0, 1, 3, 6], [0, 5, 12, 21]])
        rectangle_sum = acm2dim_helper(a)
        self.assertEqual(rectangle_sum(0, 1, 2, 3), 16)

    def test_prefix_sum_3d(self):
        a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        prefix_sum = accumulate3dim(a)
        self.assertEqual(prefix_sum[2][2][2], 36)
        cuboid_sum = acm3dim_helper(a)
        self.assertEqual(cuboid_sum(0, 0, 1, 2, 2, 2), 20)

    def test_imos(self):
        add, build = imos_helper(5)
        add(1, 4, 2)
        add(2, 5, 3)
        self.assertEqual(build(), [0, 2, 5, 5, 3])

    def test_imos_2d(self):
        add, build = imos2d_helper(3, 4)
        add(0, 0, 2, 3, 2)
        add(1, 2, 3, 4, 3)
        expected = [[2, 2, 2, 0], [2, 2, 5, 3], [0, 0, 3, 3]]
        self.assertEqual(build(), expected)

    def test_imos_3d(self):
        add, build = imos3d_helper(2, 2, 3)
        add(0, 0, 0, 2, 1, 2, 2)
        add(1, 0, 1, 2, 2, 3, 3)
        expected = [[[2, 2, 0], [0, 0, 0]], [[2, 5, 3], [0, 3, 3]]]
        self.assertEqual(build(), expected)


if __name__ == '__main__':
    unittest.main()
