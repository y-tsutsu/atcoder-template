from fractions import Fraction
from math import sqrt
import unittest

from tests.math._loader import load_math_module


class TestQuadratic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        module = load_math_module('quadratic')
        cls.quadratic = staticmethod(module['quadratic'])
        cls.quadratic_integer_roots = staticmethod(module['quadratic_integer_roots'])
        cls.two_roots = module['TWO_ROOTS']
        cls.one_root = module['ONE_ROOT']
        cls.no_real_roots = module['NO_REAL_ROOTS']
        cls.infinite_solutions = module['INFINITE_SOLUTIONS']

    def test_two_rational_roots(self):
        self.assertEqual(
            self.quadratic(1, -5, 6),
            (self.two_roots, (Fraction(2), Fraction(3))),
        )
        self.assertEqual(
            self.quadratic(2, 1, -1),
            (self.two_roots, (Fraction(-1), Fraction(1, 2))),
        )

    def test_two_irrational_roots(self):
        status, roots = self.quadratic(1, 0, -2)
        self.assertEqual(status, self.two_roots)
        self.assertAlmostEqual(roots[0], -sqrt(2))
        self.assertAlmostEqual(roots[1], sqrt(2))

    def test_repeated_root(self):
        self.assertEqual(
            self.quadratic(2, 4, 2),
            (self.one_root, (Fraction(-1),)),
        )

    def test_no_real_roots(self):
        self.assertEqual(
            self.quadratic(1, 0, 1),
            (self.no_real_roots, ()),
        )

    def test_linear_equation(self):
        self.assertEqual(
            self.quadratic(0, 2, -1),
            (self.one_root, (Fraction(1, 2),)),
        )

    def test_degenerate_equation(self):
        self.assertEqual(
            self.quadratic(0, 0, 1),
            (self.no_real_roots, ()),
        )
        self.assertEqual(
            self.quadratic(0, 0, 0),
            (self.infinite_solutions, None),
        )

    def test_integer_roots(self):
        self.assertEqual(self.quadratic_integer_roots(1, -5, 6), (2, 3))
        self.assertEqual(self.quadratic_integer_roots(2, 1, -1), (-1,))
        self.assertEqual(self.quadratic_integer_roots(1, 0, -2), ())
        self.assertEqual(self.quadratic_integer_roots(1, 0, 1), ())
        self.assertEqual(self.quadratic_integer_roots(0, 2, -4), (2,))
        self.assertIsNone(self.quadratic_integer_roots(0, 0, 0))


if __name__ == '__main__':
    unittest.main()
