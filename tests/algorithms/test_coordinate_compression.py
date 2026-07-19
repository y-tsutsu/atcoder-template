import unittest

from algorithms.coordinate_compression import compress


class TestCoordinateCompression(unittest.TestCase):
    def test_compress(self):
        self.assertEqual(compress([50, 10, 50, -3]), [2, 1, 2, 0])

    def test_start(self):
        self.assertEqual(compress([50, 10, 50, -3], start=1), [3, 2, 3, 1])

    def test_empty(self):
        self.assertEqual(compress([]), [])


if __name__ == '__main__':
    unittest.main()
