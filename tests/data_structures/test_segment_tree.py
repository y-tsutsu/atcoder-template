import unittest

from data_structures.dual_seg_tree import DualSegTree
from data_structures.lazy_seg_tree import LazySegTree
from data_structures.seg_tree import SegTree
from data_structures.seg_tree import SegTreeAddRange


class TestSegmentTree(unittest.TestCase):
    def test_segment_tree(self):
        st = SegTree(lambda x, y: x + y, lambda: 0, 5, [1, 2, 3, 4, 5])
        self.assertEqual(st.prod(1, 4), 9)
        self.assertEqual(st.all_prod(), 15)
        st.set(2, 10)
        st.update(0, 4, lambda x, y: x + y)
        self.assertEqual([st.get(i) for i in range(5)], [5, 2, 10, 4, 5])
        self.assertEqual(st.prod(0, 5), 26)

    def test_segment_tree_add_range(self):
        st = SegTreeAddRange(5)
        st.add(1, 4, 2)
        st.add(2, 5, 3)
        self.assertEqual([st.get(i) for i in range(5)], [0, 2, 5, 5, 3])

    def test_dual_segment_tree(self):
        st = DualSegTree(lambda x, y: x + y, lambda: 0, 5, [1, 2, 3, 4, 5])
        st.apply(1, 4, 10)
        st.apply(2, 5, 20)
        self.assertEqual([st.get(i) for i in range(5)], [1, 12, 33, 34, 25])
        st.set(2, 100)
        self.assertEqual(st.get(2), 130)

    @staticmethod
    def make_lazy_segment_tree(values):
        return LazySegTree(
            lambda x, y: (x[0] + y[0], x[1] + y[1]),
            lambda: (0, 0),
            len(values),
            lambda f, x: (x[0] + x[1] * f, x[1]),
            lambda f, g: f + g,
            lambda: 0,
            [(x, 1) for x in values],
        )

    def test_lazy_segment_tree(self):
        st = self.make_lazy_segment_tree([1, 2, 3, 4, 5])
        st.apply(1, 4, 10)
        st.apply_point(0, 3)
        self.assertEqual(st.prod(0, 5)[0], 48)
        self.assertEqual(st.prod(1, 4)[0], 39)
        self.assertEqual(st.get(0)[0], 4)
        st.set(4, (20, 1))
        self.assertEqual(st.all_prod()[0], 63)

    def test_lazy_segment_tree_max_right(self):
        st = self.make_lazy_segment_tree([1, 2, 3, 4])
        self.assertEqual(st.max_right(0, lambda x: x[0] <= 6), 3)

    def test_lazy_segment_tree_min_left(self):
        st = self.make_lazy_segment_tree([1, 2, 3, 4])
        self.assertEqual(st.min_left(4, lambda x: x[0] <= 7), 2)


if __name__ == '__main__':
    unittest.main()
