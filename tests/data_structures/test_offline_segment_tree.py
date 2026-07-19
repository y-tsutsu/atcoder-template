import unittest

from data_structures.offline_dual_seg_tree import OfflineDualSegTree
from data_structures.offline_dual_seg_tree import OfflineDualSegTreeMax
from data_structures.offline_dual_seg_tree import OfflineDualSegTreeMin
from data_structures.offline_dual_seg_tree_2d import OfflineDualSegTree2D
from data_structures.offline_dual_seg_tree_2d import OfflineDualSegTree2DMax
from data_structures.offline_dual_seg_tree_2d import OfflineDualSegTree2DMin


class TestOfflineSegmentTree(unittest.TestCase):
    def test_offline_dual_segment_tree(self):
        st = OfflineDualSegTree(lambda x, y: x + y, lambda: 0, 5)
        st.apply(1, 4, 2)
        st.apply(2, 5, 3)
        self.assertEqual(st.build(), [0, 2, 5, 5, 3])

    def test_specialized_offline_dual_segment_tree(self):
        max_st = OfflineDualSegTreeMax(5)
        min_st = OfflineDualSegTreeMin(5)
        for st in [max_st, min_st]:
            st.apply(1, 4, 5)
            st.apply(2, 5, 3)
        self.assertEqual(max_st.build(), [-(1 << 62), 5, 5, 5, 3])
        self.assertEqual(min_st.build(), [1 << 62, 5, 3, 3, 3])

    def test_offline_dual_segment_tree_2d(self):
        st = OfflineDualSegTree2D(lambda x, y: x + y, lambda: 0, 3, 4)
        st.apply(0, 1, 2, 3, 2)
        st.apply(1, 2, 3, 4, 3)
        self.assertEqual(st.build(), [[0, 2, 2, 0], [0, 2, 5, 3], [0, 0, 3, 3]])

    def test_specialized_offline_dual_segment_tree_2d(self):
        max_st = OfflineDualSegTree2DMax(2, 3)
        min_st = OfflineDualSegTree2DMin(2, 3)
        for st in [max_st, min_st]:
            st.apply(0, 0, 2, 2, 5)
            st.apply(1, 1, 2, 3, 3)
        self.assertEqual(max_st.build(), [[5, 5, -(1 << 62)], [5, 5, 3]])
        self.assertEqual(min_st.build(), [[5, 5, 1 << 62], [5, 3, 3]])


if __name__ == '__main__':
    unittest.main()
