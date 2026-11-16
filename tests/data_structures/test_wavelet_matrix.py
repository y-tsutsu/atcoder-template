import random
import unittest

from data_structures.wavelet_matrix import WaveletMatrix


class TestWaveletMatrix(unittest.TestCase):
    def test_matches_naive(self):
        rng = random.Random(0)
        for n in range(25):
            a = [rng.randrange(-5, 6) for _ in range(n)]
            wm = WaveletMatrix(a)
            for _ in range(50):
                l = rng.randrange(n + 1)
                r = rng.randrange(l, n + 1)
                b = sorted(a[l:r])
                x = rng.randrange(-7, 8)
                y = rng.randrange(x, 9)
                self.assertEqual(wm.count_less(l, r, x), sum(v < x for v in b))
                self.assertEqual(wm.range_count(l, r, x, y), sum(x <= v < y for v in b))
                self.assertEqual(wm.count(l, r, x), b.count(x))
                self.assertEqual(wm.prev_value(l, r, x), max((v for v in b if v < x), default=None))
                self.assertEqual(wm.next_value(l, r, x), min((v for v in b if v >= x), default=None))
                for k, v in enumerate(b):
                    self.assertEqual(wm.kth_smallest(l, r, k), v)
                    self.assertEqual(wm.kth_largest(l, r, k), b[-1 - k])

    def test_single_value_and_large_integers(self):
        for a in [[7], [7] * 5, [-10**30, 10**30, 0, -10**30]]:
            original = a[:]
            wm = WaveletMatrix(a)
            self.assertEqual(a, original)
            for k, v in enumerate(sorted(a)):
                self.assertEqual(wm.kth_smallest(0, len(a), k), v)

    def test_invalid_queries(self):
        wm = WaveletMatrix([1, 2])
        for k in [-1, 2]:
            with self.assertRaises(AssertionError):
                wm.kth_smallest(0, 2, k)
            with self.assertRaises(AssertionError):
                wm.kth_largest(0, 2, k)
        with self.assertRaises(AssertionError):
            wm.kth_smallest(0, 0, 0)
        with self.assertRaises(AssertionError):
            wm.count_less(-1, 2, 0)
        with self.assertRaises(AssertionError):
            wm.range_count(0, 2, 3, 1)


if __name__ == '__main__':
    unittest.main()
