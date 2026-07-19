import math
import unittest

from geometry.geometry import Sfol
from geometry.geometry import calc_distance
from geometry.geometry import calc_intersection_point
from geometry.geometry import calc_triangle_area
from geometry.geometry import calc_triangle_area_origin
from geometry.geometry import intersect
from geometry.geometry import is_collinear
from geometry.geometry import rotate
from geometry.geometry import rotate_origin


class TestGeometry(unittest.TestCase):
    def test_collinear_and_area(self):
        self.assertTrue(is_collinear((0, 0), (1, 2), (2, 4)))
        self.assertFalse(is_collinear((0, 0), (1, 2), (2, 5)))
        self.assertEqual(calc_triangle_area((0, 0), (4, 0), (0, 3)), 6)
        self.assertEqual(calc_triangle_area_origin((4, 0), (0, 3)), 6)

    def test_rotate(self):
        x, y = rotate_origin(1, 0, math.pi / 2)
        self.assertAlmostEqual(x, 0)
        self.assertAlmostEqual(y, 1)
        x, y = rotate(2, 1, 1, 1, math.pi / 2)
        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, 2)

    def test_standard_form_of_line(self):
        self.assertEqual(Sfol(0, 1, 2, 1), Sfol(5, 1, 8, 1))
        self.assertEqual(Sfol(2, 0, 2, 3), Sfol(2, -5, 2, 10))
        with self.assertRaises(AssertionError):
            Sfol(1, 1, 1, 1)

    def test_distance_to_segment(self):
        self.assertEqual(calc_distance(5, 3, 0, 0, 10, 0), 3)
        self.assertEqual(calc_distance(3, 5, 0, 0, 0, 10), 3)
        self.assertEqual(calc_distance(-3, 4, 0, 0, 10, 0), 5)
        self.assertEqual(calc_distance(3, 4, 0, 0, 0, 0), 5)
        self.assertAlmostEqual(calc_distance(0, 1, 0, 0, 2, 2), math.sqrt(0.5))

    def test_intersection_point(self):
        x, y = calc_intersection_point(5, 3, 0, 0, 10, 0)
        self.assertAlmostEqual(x, 5)
        self.assertAlmostEqual(y, 0)

    def test_segment_intersection(self):
        self.assertTrue(intersect(0, 0, 2, 2, 0, 2, 2, 0))
        self.assertTrue(intersect(0, 0, 2, 0, 2, 0, 3, 1))
        self.assertTrue(intersect(0, 0, 3, 0, 1, 0, 4, 0))
        self.assertFalse(intersect(0, 0, 1, 0, 2, 0, 3, 0))
        self.assertTrue(intersect(0, 1, 0, 1, 0, 0, 0, 2))
        self.assertFalse(intersect(0, 3, 0, 3, 0, 0, 0, 2))


if __name__ == '__main__':
    unittest.main()
