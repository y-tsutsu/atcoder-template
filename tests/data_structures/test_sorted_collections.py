import bisect
import random
import unittest

from data_structures.bucket_list import BucketList
from data_structures.sorted_multiset import SortedMultiset
from data_structures.sorted_set import SortedSet


class TestSortedCollections(unittest.TestCase):
    def test_sorted_set(self):
        s = SortedSet([3, 1, 2, 2])
        self.assertEqual(list(s), [1, 2, 3])
        self.assertFalse(s.add(2))
        self.assertTrue(s.add(4))
        self.assertEqual((s.lt(2), s.le(2), s.gt(2), s.ge(2)), (1, 2, 3, 2))
        self.assertEqual((s.index(3), s.index_right(3)), (2, 3))
        self.assertEqual(s.pop(1), 2)
        self.assertEqual(list(s), [1, 3, 4])

    def test_sorted_multiset(self):
        s = SortedMultiset([3, 1, 2, 2])
        self.assertEqual(list(s), [1, 2, 2, 3])
        self.assertEqual(s.count(2), 2)
        s.add(2)
        s.discard(3)
        self.assertEqual(list(s), [1, 2, 2, 2])
        self.assertEqual((s.lt(2), s.le(2), s.gt(2), s.ge(2)), (1, 2, None, 2))

    def test_sorted_multiset_matches_list(self):
        random.seed(0)
        s = SortedMultiset()
        a = []
        for _ in range(500):
            x = random.randrange(20)
            if random.randrange(2):
                s.add(x)
                bisect.insort(a, x)
            else:
                result = s.discard(x)
                if x in a:
                    a.remove(x)
                    self.assertTrue(result)
                else:
                    self.assertFalse(result)
            self.assertEqual(list(s), a)

    def test_bucket_list(self):
        bucket = BucketList(range(20))
        a = list(range(20))
        bucket.insert(5, 100)
        a.insert(5, 100)
        bucket.append(200)
        a.append(200)
        bucket[0] = -1
        a[0] = -1
        self.assertEqual(bucket.pop(-2), a.pop(-2))
        bucket.reverse()
        a.reverse()
        self.assertEqual(list(bucket), a)
        self.assertEqual(bucket.copy(), bucket)


if __name__ == '__main__':
    unittest.main()
