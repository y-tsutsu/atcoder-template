from fractions import Fraction
from math import gcd
from math import prod
import unittest

from tests.math._loader import load_math_module


class TestNumberTheory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.extgcd_module = load_math_module('extgcd')
        cls.floor_sum_module = load_math_module('floor_sum')
        cls.prime_module = load_math_module('prime')
        cls.system_module = load_math_module('system_of_equations')

    def test_extgcd(self):
        extgcd = self.extgcd_module['extgcd']
        for a in range(1, 30):
            for b in range(1, 30):
                g, x, y = extgcd(a, b)
                self.assertEqual(g, gcd(a, b))
                self.assertEqual(a * x + b * y, g)

    def test_linear_indefinite_equation(self):
        solve = self.extgcd_module['solve_linear_indefinite_equation']
        x, y = solve(6, 9, 12)
        self.assertEqual(6 * x + 9 * y, 12)
        self.assertIsNone(solve(6, 9, 10))

    def test_floor_sum_matches_naive_sum(self):
        floor_sum = self.floor_sum_module['floor_sum']
        for n in range(15):
            for m in range(1, 10):
                for a in range(10):
                    for b in range(10):
                        expected = sum((a * i + b) // m for i in range(n))
                        self.assertEqual(floor_sum(n, m, a, b), expected)

    def test_is_prime_and_primes(self):
        is_prime = self.prime_module['is_prime']
        primes = self.prime_module['primes']
        expected = [n for n in range(101) if n >= 2 and all(n % d for d in range(2, n))]
        self.assertEqual(primes(100), expected)
        for n in range(101):
            self.assertEqual(is_prime(n), n in expected)

    def test_prime_factorize(self):
        prime_factorize = self.prime_module['prime_factorize']
        is_prime = self.prime_module['is_prime']
        for n in range(1, 101):
            factors = prime_factorize(n)
            self.assertEqual(prod(factors), n)
            self.assertTrue(all(is_prime(p) for p in factors))
            self.assertEqual(factors, sorted(factors))

    def test_system_of_equations_with_unique_solution(self):
        solve = self.system_module['system_of_equations']
        unique = self.system_module['UNIQUE']

        status, (x, y) = solve(1, 1, 1, -1, 5, 1)
        self.assertEqual(status, unique)
        self.assertEqual((x, y), (3, 2))

        status, (x, y) = solve(2, 4, 1, -1, 1, 0)
        self.assertEqual(status, unique)
        self.assertEqual((x, y), (Fraction(1, 6), Fraction(1, 6)))

        status, (x, y) = solve(0, 2, 3, 0, 4, 9)
        self.assertEqual(status, unique)
        self.assertEqual((x, y), (3, 2))

    def test_system_of_equations_without_unique_solution(self):
        solve = self.system_module['system_of_equations']
        none = self.system_module['NONE']
        infinite = self.system_module['INFINITE']

        self.assertEqual(solve(1, 2, 2, 4, 3, 7), (none, None))
        self.assertEqual(solve(1, 2, 2, 4, 3, 6), (infinite, None))
        self.assertEqual(solve(0, 0, 1, 2, 0, 3), (infinite, None))
        self.assertEqual(solve(0, 0, 1, 2, 1, 3), (none, None))


if __name__ == '__main__':
    unittest.main()
