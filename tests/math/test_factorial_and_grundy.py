import unittest

from tests.math._loader import load_math_module


class TestFactorialAndGrundy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.factorial = load_math_module('count_p_in_factorial')
        cls.grundy = load_math_module('grundy')

    def test_count_p_in_factorial(self):
        count = self.factorial['count_p_in_factorial']
        self.assertEqual(count(10, 2), 8)
        self.assertEqual(count(10, 3), 4)
        self.assertEqual(count(100, 5), 24)

    def test_count_p_in_double_factorial(self):
        count = self.factorial['count_p_in_double_factorial']
        for n in range(1, 30):
            value = 1
            for x in range(n, 0, -2):
                value *= x
            for p in (2, 3, 5, 7):
                expected = 0
                while value % p == 0:
                    expected += 1
                    value //= p
                self.assertEqual(count(n, p), expected)

    def test_grundy_from_transition_function(self):
        grundy_by_transition = self.grundy['grundy_by_transition']
        actual = grundy_by_transition(10, lambda x: [x - d for d in (2, 3) if x >= d])
        self.assertEqual(actual, [0, 0, 1, 1, 2, 0, 0, 1, 1, 2, 0])

    def test_grundy_from_costs(self):
        grundy_by_moves = self.grundy['grundy_by_moves']
        self.assertEqual(grundy_by_moves(10, [2, 3]), [0, 0, 1, 1, 2, 0, 0, 1, 1, 2, 0])

    def test_grundy_range(self):
        grundy_by_range = self.grundy['grundy_by_range']
        self.assertEqual(grundy_by_range(10, 2, 3), [0, 0, 1, 1, 2, 0, 0, 1, 1, 2, 0])


if __name__ == '__main__':
    unittest.main()
