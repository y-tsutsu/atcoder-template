import unittest

from data_structures.monoid_union_find import MonoidUnionFind
from data_structures.rollback_union_find import RollbackUnionFind
from data_structures.union_find import UnionFind
from data_structures.weighted_union_find import WeightedUnionFind


class TestUnionFind(unittest.TestCase):
    def test_union_find(self):
        uf = UnionFind(5)
        uf.unite(0, 1)
        uf.unite(1, 2)
        self.assertTrue(uf.same(0, 2))
        self.assertFalse(uf.same(0, 3))
        self.assertEqual(uf.size(1), 3)
        self.assertEqual(uf.count(), 3)
        self.assertEqual(sorted(map(sorted, uf.groups())), [[0, 1, 2], [3], [4]])

    def test_rollback_union_find(self):
        uf = RollbackUnionFind(4)
        uf.unite(0, 1)
        uf.unite(1, 2)
        self.assertTrue(uf.same(0, 2))
        self.assertTrue(uf.rollback())
        self.assertFalse(uf.same(0, 2))
        uf.unite(0, 1)
        self.assertFalse(uf.rollback())

    def test_weighted_union_find(self):
        uf = WeightedUnionFind(4)
        uf.unite(0, 1, 3)
        uf.unite(1, 2, 4)
        self.assertEqual(uf.diff(0, 1), 3)
        self.assertEqual(uf.diff(0, 2), 7)
        self.assertEqual(uf.diff(2, 0), -7)
        self.assertIsNone(uf.diff(0, 3))

    def test_monoid_union_find(self):
        uf = MonoidUnionFind(4, [1, 2, 4, 8], lambda x, y: x + y)
        uf.unite(0, 1)
        uf.unite(2, 3)
        uf.unite(0, 2)
        self.assertEqual(uf.data(3), 15)
        self.assertEqual(uf.size(1), 4)
        self.assertEqual(uf.count(), 1)
        uf.set_value(2, 42)
        self.assertEqual(uf.value(0), 42)


if __name__ == '__main__':
    unittest.main()
