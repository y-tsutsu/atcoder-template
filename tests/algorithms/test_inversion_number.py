import random
import unittest

from algorithms import inversion_number
from algorithms.coordinate_compression import compress
from data_structures.binary_indexed_tree import BIT


def naive_inversion_number(a):
    return sum(a[i] > a[j] for i in range(len(a)) for j in range(i + 1, len(a)))


class TestInversionNumber(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        inversion_number.BIT = BIT
        inversion_number.compress = compress

    def test_example(self):
        self.assertEqual(inversion_number.inv_num([3, 1, 4, 1, 5]), 3)

    def test_sorted(self):
        self.assertEqual(inversion_number.inv_num([1, 2, 3, 4]), 0)
        self.assertEqual(inversion_number.inv_num([4, 3, 2, 1]), 6)

    def test_empty(self):
        self.assertEqual(inversion_number.inv_num([]), 0)

    def test_matches_naive_inversion_number(self):
        random.seed(0)
        for n in range(20):
            for _ in range(20):
                a = [random.randrange(-5, 6) for _ in range(n)]
                self.assertEqual(inversion_number.inv_num(a), naive_inversion_number(a))


if __name__ == '__main__':
    unittest.main()
