import unittest

from data_structures.bitset import BitSet
from data_structures.deque import Deque
from data_structures.doubling import Doubling
from data_structures.doubling import DoublingWeight
from data_structures.secure_hash_int import SecureHashInt


class TestBasicStructures(unittest.TestCase):
    def test_bitset(self):
        a = BitSet(5)
        a[1] = 1
        a[3] = 1
        self.assertEqual(str(a), '01010')
        self.assertEqual([(a << 1)[i] for i in range(5)], [0, 0, 1, 0, 1])
        b = BitSet(5)
        b[3] = 1
        b[4] = 1
        self.assertEqual(str(a & b), '01000')
        self.assertEqual(str(a | b), '11010')

    def test_bitset_with_negative_index(self):
        a = BitSet(3, negative_index=True)
        a[-2] = 1
        a[1] = 1
        self.assertEqual(a[-2], 1)
        self.assertEqual(a[1], 1)
        self.assertEqual(len(str(a)), 6)

    def test_deque(self):
        q = Deque(capacity=2)
        q.append(2)
        q.appendleft(1)
        q.append(3)
        q.appendleft(0)
        self.assertEqual(list(q), [0, 1, 2, 3])
        self.assertEqual(q[-1], 3)
        q[1] = 10
        self.assertEqual(q.popleft(), 0)
        self.assertEqual(q.pop(), 3)
        self.assertEqual(list(q), [10, 2])

    def test_doubling(self):
        next_ = [1, 2, 3, 0]
        doubling = Doubling(next_, max_=4)
        self.assertEqual(doubling.query(0, 7), 3)

    def test_doubling_weight(self):
        next_ = [1, 2, 3, 0]
        weight = [10, 20, 30, 40]
        doubling = DoublingWeight(next_, weight, max_=4)
        self.assertEqual(doubling.query(0, 5), (1, 110))

    def test_secure_hash_int(self):
        x = SecureHashInt(42)
        self.assertEqual(x, 42)
        self.assertEqual(hash(x), hash(x))
        self.assertEqual({x: 'value'}[SecureHashInt(42)], 'value')


if __name__ == '__main__':
    unittest.main()
