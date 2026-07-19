from math import comb as math_comb
from math import perm as math_perm
import unittest

from tests.math._loader import load_math_module


class TestCombinations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_math_module('combinations')

    def test_perm(self):
        perm = self.module['perm']
        factorial_perm = self.module['factorial_perm']
        for n in range(10):
            for r in range(n + 1):
                expected = math_perm(n, r)
                self.assertEqual(perm(n, r), expected)
                self.assertEqual(factorial_perm(n, r), expected)

    def test_comb(self):
        comb = self.module['comb']
        factorial_comb = self.module['factorial_comb']
        pascal_comb = self.module['pascal_comb']
        for n in range(10):
            for r in range(n + 1):
                expected = math_comb(n, r)
                self.assertEqual(comb(n, r), expected)
                self.assertEqual(factorial_comb(n, r), expected)
                self.assertEqual(pascal_comb(n, r), expected)

    def test_invalid_comb(self):
        comb = self.module['comb']
        self.assertEqual(comb(3, -1), 0)
        self.assertEqual(comb(3, 4), 0)
        self.assertEqual(comb(-1, 0), 0)

    def test_combination_with_repetition(self):
        combr = self.module['combr']
        self.assertEqual(combr(0, 0), 1)
        self.assertEqual(combr(0, 1), 0)
        for n in range(1, 8):
            for r in range(8):
                self.assertEqual(combr(n, r), math_comb(n + r - 1, r))


if __name__ == '__main__':
    unittest.main()
