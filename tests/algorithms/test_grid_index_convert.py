import unittest

from algorithms.grid_index_convert import itop
from algorithms.grid_index_convert import pack
from algorithms.grid_index_convert import ptoi
from algorithms.grid_index_convert import unpack


class TestGridIndexConvert(unittest.TestCase):
    def test_2d_round_trip(self):
        for h in range(1, 5):
            for w in range(1, 5):
                for i in range(h):
                    for j in range(w):
                        self.assertEqual(itop(ptoi(i, j, w), w), (i, j))

    def test_3d_round_trip(self):
        for d in range(1, 4):
            for h in range(1, 4):
                for w in range(1, 4):
                    for i in range(d):
                        for j in range(h):
                            for k in range(w):
                                self.assertEqual(unpack(pack(i, j, k, h, w), h, w), (i, j, k))


if __name__ == '__main__':
    unittest.main()
