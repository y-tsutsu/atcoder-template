import random
import unittest

from algorithms.bisect_lambda import bisect_ng_ok
from algorithms.bisect_lambda import bisect_ok_ng


class TestBisectLambda(unittest.TestCase):
    def test_bisect_ng_ok(self):
        self.assertEqual(bisect_ng_ok(0, 10, lambda x: x >= 4), 4)
        self.assertEqual(bisect_ng_ok(0, 10, lambda x: True), 0)
        self.assertEqual(bisect_ng_ok(0, 10, lambda x: False), 11)

    def test_bisect_ok_ng(self):
        self.assertEqual(bisect_ok_ng(0, 10, lambda x: x <= 6), 6)
        self.assertEqual(bisect_ok_ng(0, 10, lambda x: True), 10)
        self.assertEqual(bisect_ok_ng(0, 10, lambda x: False), -1)

    def test_random_boundary(self):
        random.seed(0)
        for _ in range(100):
            boundary = random.randrange(-20, 21)
            self.assertEqual(bisect_ng_ok(-20, 20, lambda x: x >= boundary), boundary)
            self.assertEqual(bisect_ok_ng(-20, 20, lambda x: x <= boundary), boundary)


if __name__ == '__main__':
    unittest.main()
