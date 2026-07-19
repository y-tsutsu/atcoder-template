import unittest

from algorithms.list_utils import chunks
from algorithms.list_utils import flatten
from algorithms.list_utils import normalize
from algorithms.list_utils import rotate_ccw
from algorithms.list_utils import rotate_cw
from algorithms.list_utils import scatter
from algorithms.list_utils import transpose


class TestListUtils(unittest.TestCase):
    def test_flatten_and_chunks(self):
        self.assertEqual(flatten([[1, 2], [3, 4]]), [1, 2, 3, 4])
        self.assertEqual(chunks([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_scatter(self):
        self.assertEqual(scatter([0, 1, 2, 3, 4], 2), [[0, 2, 4], [1, 3]])

    def test_rotate_rectangle(self):
        a = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(rotate_cw(a), [[4, 1], [5, 2], [6, 3]])
        self.assertEqual(rotate_ccw(a), [[3, 6], [2, 5], [1, 4]])
        self.assertEqual(rotate_ccw(rotate_cw(a)), a)

    def test_transpose(self):
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6]]), [(1, 4), (2, 5), (3, 6)])

    def test_normalize(self):
        a = ['....', '.##.', '..#.', '....']
        self.assertEqual(normalize(a), [['#', '#'], ['.', '#']])
        self.assertEqual(normalize(['...', '...']), [])


if __name__ == '__main__':
    unittest.main()
