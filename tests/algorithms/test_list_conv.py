import unittest

from algorithms.list_conv import chunks
from algorithms.list_conv import flatten
from algorithms.list_conv import lrotate
from algorithms.list_conv import normalize
from algorithms.list_conv import rrotate
from algorithms.list_conv import scatter
from algorithms.list_conv import transpose


class TestListConv(unittest.TestCase):
    def test_flatten_and_chunks(self):
        self.assertEqual(flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(chunks([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_scatter(self):
        self.assertEqual(scatter([0, 1, 2, 3, 4], 2), [[0, 2, 4], [1, 3]])

    def test_rotate_rectangle(self):
        a = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(rrotate(a), [[4, 1], [5, 2], [6, 3]])
        self.assertEqual(lrotate(a), [[3, 6], [2, 5], [1, 4]])
        self.assertEqual(lrotate(rrotate(a)), a)

    def test_transpose(self):
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6]]), [(1, 4), (2, 5), (3, 6)])

    def test_normalize(self):
        a = ['....', '.##.', '..#.', '....']
        self.assertEqual(normalize(a), [['#', '#'], ['.', '#']])
        self.assertEqual(normalize(['...', '...']), [])


if __name__ == '__main__':
    unittest.main()
