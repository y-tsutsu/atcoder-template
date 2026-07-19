import unittest

from algorithms.range import Range


class TestRange(unittest.TestCase):
    def test_sequence_operations(self):
        interval = Range(2, 5)
        self.assertEqual(list(interval), [2, 3, 4])
        self.assertEqual(list(reversed(interval)), [4, 3, 2])
        self.assertEqual(len(interval), 3)
        self.assertEqual(str(interval), '(2, 5)')

    def test_contains(self):
        interval = Range(2, 5)
        self.assertIn(2, interval)
        self.assertNotIn(5, interval)
        self.assertIn(Range(3, 5), interval)
        self.assertNotIn(Range(1, 3), interval)

    def test_overlap_and_intersection(self):
        a = Range(1, 5)
        b = Range(3, 7)
        self.assertTrue(a.overlaps(b))
        self.assertEqual(a.intersection(b), Range(3, 5))
        self.assertFalse(a.overlaps(Range(5, 8)))
        self.assertIsNone(a.intersection(Range(5, 8)))

    def test_union_and_gap(self):
        a = Range(1, 5)
        self.assertEqual(a.union(Range(5, 8)), Range(1, 8))
        self.assertIsNone(a.union(Range(6, 8)))
        self.assertEqual(a.gap(Range(5, 8)), 0)
        self.assertEqual(a.gap(Range(7, 9)), 2)
        self.assertEqual(a.gap(Range(3, 6)), -1)

    def test_order(self):
        intervals = [Range(2, 4), Range(1, 5), Range(1, 3)]
        self.assertEqual(sorted(intervals), [Range(1, 3), Range(1, 5), Range(2, 4)])

    def test_empty_and_invalid_range(self):
        self.assertEqual(len(Range(2, 2)), 0)
        with self.assertRaises(AssertionError):
            Range(3, 2)


if __name__ == '__main__':
    unittest.main()
