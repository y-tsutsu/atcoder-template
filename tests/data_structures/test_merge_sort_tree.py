import random
import unittest

from data_structures.merge_sort_tree import MergeSortTree


class TestMergeSortTree(unittest.TestCase):
    def test_query(self):
        a = [5, 1, 4, 2, 3, 2]
        tree = MergeSortTree(len(a), a)
        self.assertEqual(tree.query(1, 5, 3), 3)
        self.assertEqual(tree.queryex(0, 6, 2, 4), 4)

    def test_matches_naive_count(self):
        random.seed(0)
        a = [random.randrange(-10, 11) for _ in range(50)]
        tree = MergeSortTree(len(a), a)
        for _ in range(100):
            s = random.randrange(len(a) + 1)
            e = random.randrange(s, len(a) + 1)
            x = random.randrange(-12, 13)
            y = random.randrange(x, 13)
            self.assertEqual(tree.query(s, e, x), sum(v <= x for v in a[s:e]))
            self.assertEqual(tree.queryex(s, e, x, y), sum(x <= v <= y for v in a[s:e]))


if __name__ == '__main__':
    unittest.main()
