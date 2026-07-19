import random
import unittest

from algorithms.convolution import convolution


def naive_convolution(a, b, mod=998244353):
    if not a or not b:
        return []
    result = [0 for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] = (result[i + j] + x * y) % mod
    return result


class TestConvolution(unittest.TestCase):
    def test_example(self):
        self.assertEqual(convolution([1, 2], [3, 4]), [3, 10, 8])

    def test_different_lengths(self):
        self.assertEqual(convolution([1, 2, 3], [4]), [4, 8, 12])

    def test_empty(self):
        self.assertEqual(convolution([], [1, 2]), [])
        self.assertEqual(convolution([1, 2], []), [])

    def test_matches_naive_convolution(self):
        random.seed(0)
        for n in range(1, 10):
            for m in range(1, 10):
                a = [random.randrange(-100, 101) for _ in range(n)]
                b = [random.randrange(-100, 101) for _ in range(m)]
                self.assertEqual(convolution(a, b), naive_convolution(a, b))


if __name__ == '__main__':
    unittest.main()
