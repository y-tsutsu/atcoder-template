import unittest

from tests.string._loader import load_string_module


class TestRollingHash(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        module = load_string_module('rolling_hash')
        cls.RollingHash = module['RollingHash']
        cls.SegRollingHash = module['SegRollingHash']

    def test_same_substrings_have_same_hash(self):
        rolling_hash = self.RollingHash('abracadabra', base=137)
        self.assertEqual(rolling_hash.get_hash(0, 4), rolling_hash.get_hash(7, 11))
        self.assertNotEqual(rolling_hash.get_hash(0, 3), rolling_hash.get_hash(3, 6))

    def test_segment_tree_hash_matches_rolling_hash(self):
        s = 'abacabadabacaba'
        rolling_hash = self.RollingHash(s, base=137)
        seg_hash = self.SegRollingHash(s, base=137)
        for le in range(len(s) + 1):
            for ri in range(le, len(s) + 1):
                forward, reverse = seg_hash.get_hash(le, ri)
                self.assertEqual(forward, rolling_hash.get_hash(le, ri))
                self.assertEqual(forward == reverse, s[le:ri] == s[le:ri][::-1])

    def test_update(self):
        s = list('abcba')
        rolling_hash = self.SegRollingHash(''.join(s), base=137)
        self.assertEqual(*rolling_hash.get_hash(0, 5))
        rolling_hash.set(0, 'z')
        s[0] = 'z'
        forward, reverse = rolling_hash.get_hash(0, 5)
        self.assertNotEqual(forward, reverse)
        rolling_hash.set(4, 'z')
        s[4] = 'z'
        self.assertEqual(*rolling_hash.get_hash(0, 5))


if __name__ == '__main__':
    unittest.main()
