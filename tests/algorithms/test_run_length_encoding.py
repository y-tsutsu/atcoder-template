import unittest

from algorithms.run_length_encoding import rle


class TestRunLengthEncoding(unittest.TestCase):
    def test_string(self):
        self.assertEqual(rle('aaabbc'), [('a', 3), ('b', 2), ('c', 1)])

    def test_list(self):
        self.assertEqual(rle([1, 1, 2, 1]), [(1, 2), (2, 1), (1, 1)])

    def test_empty(self):
        self.assertEqual(rle([]), [])


if __name__ == '__main__':
    unittest.main()
