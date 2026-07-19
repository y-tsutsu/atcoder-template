import unittest

from algorithms.flat_list_2d import FlatList2D


class TestFlatList2D(unittest.TestCase):
    def test_get_and_set(self):
        a = FlatList2D(2, 3, initial=-1)
        a[1, 2] = 7
        self.assertEqual(a[0, 0], -1)
        self.assertEqual(a[1, 2], 7)
        self.assertEqual(list(a), [-1, -1, -1, -1, -1, 7])
        self.assertEqual(len(a), 6)
        self.assertIn(7, a)

    def test_copy_is_independent(self):
        a = FlatList2D(2, 2)
        b = a.copy()
        b[0, 0] = 1
        self.assertEqual(a[0, 0], 0)
        self.assertNotEqual(a, b)

    def test_string(self):
        a = FlatList2D(2, 2)
        a[1, 0] = 3
        self.assertEqual(str(a), '[0, 0]\n[3, 0]')


if __name__ == '__main__':
    unittest.main()
