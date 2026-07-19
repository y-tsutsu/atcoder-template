from math import comb
import unittest

from tests.math._loader import load_math_module


class TestModularCalculation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_math_module('mcalc')

    def test_mpow(self):
        mpow = self.module['mpow']
        for mod in (2, 7, 998244353):
            for a in range(10):
                for b in range(10):
                    self.assertEqual(mpow(a, b, mod), pow(a, b, mod))

    def test_mpow_of_mpow(self):
        mpow_of_mpow = self.module['mpow_of_mpow']
        mod = 101
        for a in range(1, 10):
            for b in range(1, 6):
                for c in range(1, 5):
                    self.assertEqual(mpow_of_mpow(a, b, c, mod), pow(a, b ** c, mod))

    def test_mdiv(self):
        mdiv = self.module['mdiv']
        mod = 101
        for n in range(20):
            for r in range(1, 20):
                self.assertEqual(mdiv(n, r, mod) * r % mod, n % mod)

    def test_mdiv2(self):
        mdiv2 = self.module['mdiv2']
        for mod in range(2, 10):
            for r in range(1, 10):
                for q in range(10):
                    n = q * r
                    self.assertEqual(mdiv2(n, r, mod), q % mod)

    def test_mcomb(self):
        mcomb = self.module['mcomb']
        mcombr = self.module['mcombr']
        mod = 101
        for n in range(20):
            for r in range(n + 1):
                self.assertEqual(mcomb(n, r, mod), comb(n, r) % mod)
        self.assertEqual(mcomb(3, 4, mod), 0)
        self.assertEqual(mcombr(0, 0, mod), 1)
        self.assertEqual(mcombr(5, 3, mod), comb(7, 3) % mod)

    def test_precalculated_combinations(self):
        mod = 101
        for class_name in ('MComb', 'MCombPascal'):
            table = self.module[class_name](30, mod)
            for n in range(20):
                for r in range(n + 1):
                    self.assertEqual(table.comb(n, r), comb(n, r) % mod)
            self.assertEqual(table.combr(5, 3), comb(7, 3))
            self.assertEqual(table.split(7, 3), comb(6, 2))
            self.assertEqual(table.split0(7, 3), comb(9, 2))

    def test_maccumulate(self):
        maccumulate = self.module['maccumulate']
        self.assertEqual(maccumulate([7, 8, 9], 10), [0, 7, 5, 4])

    def test_geometric_sum(self):
        for name in ('mgeosum', 'mgeosummemo'):
            mgeosum = self.module[name]
            for n in range(1, 20):
                expected = sum(3 * 5 ** i for i in range(n)) % 101
                self.assertEqual(mgeosum(3, 5, n, 101), expected)

    def test_repunit(self):
        repunit = self.module['repunit']
        for n in range(1, 20):
            self.assertEqual(repunit(n, 37), int('1' * n) % 37)

    def test_linear_congruence(self):
        linear_congruence = self.module['linear_congruence']
        self.assertEqual(linear_congruence(6, 8, 14), (6, 7))
        self.assertIsNone(linear_congruence(6, 9, 14))


if __name__ == '__main__':
    unittest.main()
