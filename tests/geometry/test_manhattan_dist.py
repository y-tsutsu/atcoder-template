import random
import unittest
from sys import maxsize

from data_structures.seg_tree import SegTree
from geometry import manhattan_dist
from geometry.manhattan_dist import manhattan_max
from geometry.manhattan_dist import rotate_45_deg


def naive_nearest(points):
    return [min((abs(x - u) + abs(y - v) for j, (u, v) in enumerate(points) if i != j), default=maxsize)
            for i, (x, y) in enumerate(points)]


class TestManhattanDistance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        manhattan_dist.SegTree = SegTree

    def test_rotate_45_degrees(self):
        self.assertEqual(rotate_45_deg([(2, 1), (-1, 3)]), [(3, 1), (2, -4)])

    def test_maximum_distance(self):
        points = [(0, 0), (2, 1), (-1, 3)]
        self.assertEqual(manhattan_max(points), 5)

    def test_nearest_distance_keeps_input_order(self):
        xs = [10, 0, 5]
        ys = [0, 1, 2]
        self.assertEqual(manhattan_dist.manhattan_mst(3, xs, ys), [7, 6, 6])

    def test_nearest_distance_with_arbitrary_coordinates(self):
        xs = [0, 1, -5]
        ys = [100, -100, 3]
        points = list(zip(xs, ys))
        self.assertEqual(manhattan_dist.manhattan_mst(3, xs, ys), naive_nearest(points))

    def test_nearest_distance_matches_naive(self):
        random.seed(0)
        for n in range(1, 20):
            for _ in range(20):
                points = [(random.randrange(-20, 21), random.randrange(-20, 21)) for _ in range(n)]
                xs = [x for x, _ in points]
                ys = [y for _, y in points]
                self.assertEqual(manhattan_dist.manhattan_mst(n, xs, ys), naive_nearest(points))


if __name__ == '__main__':
    unittest.main()
