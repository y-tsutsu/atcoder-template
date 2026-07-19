import unittest

from graph.min_plus import INF
from graph.min_plus import min_plus_mul
from graph.min_plus import min_plus_pow


class TestMinPlus(unittest.TestCase):
    def test_mul(self):
        a = [[0, 3], [2, INF]]
        b = [[1, 5], [4, 0]]
        self.assertEqual(min_plus_mul(a, b), [[1, 3], [3, 7]])

    def test_pow_zero(self):
        a = [[1, 2], [3, 4]]
        self.assertEqual(min_plus_pow(a, 0), [[0, INF], [INF, 0]])

    def test_exact_number_of_steps(self):
        a = [
            [5, 2, 8],
            [1, 4, 3],
            [6, 2, 7],
        ]
        self.assertEqual(
            min_plus_pow(a, 3),
            [[7, 5, 9], [4, 7, 6], [7, 5, 9]],
        )

    def test_input_is_not_modified(self):
        a = [[0, 1], [2, 0]]
        original = [row[:] for row in a]
        min_plus_pow(a, 3)
        self.assertEqual(a, original)


if __name__ == '__main__':
    unittest.main()
