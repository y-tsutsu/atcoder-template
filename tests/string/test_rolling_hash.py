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

    def test_equal_matches_string_comparison(self):
        s = 'abacabadabacaba'
        rolling_hash = self.RollingHash(s, base=137)
        for s1 in range(len(s) + 1):
            for s2 in range(len(s) + 1):
                for length in range(min(len(s) - s1, len(s) - s2) + 1):
                    expected = s[s1:s1 + length] == s[s2:s2 + length]
                    self.assertEqual(
                        rolling_hash.equal(s1, s1 + length, s2, s2 + length),
                        expected,
                    )

    def test_lcp_matches_naive_comparison(self):
        s = 'abacabadabacaba'
        rolling_hash = self.RollingHash(s, base=137)
        for i in range(len(s) + 1):
            for j in range(len(s) + 1):
                expected = 0
                while i + expected < len(s) and j + expected < len(s):
                    if s[i + expected] != s[j + expected]:
                        break
                    expected += 1
                self.assertEqual(rolling_hash.lcp(i, j), expected)
                self.assertEqual(rolling_hash.lcp(i, j, 3), min(expected, 3))

    def test_palindrome_matches_naive_comparison(self):
        s = 'abacabadabacaba'
        rolling_hash = self.RollingHash(s, base=137)
        for le in range(len(s) + 1):
            for ri in range(le, len(s) + 1):
                self.assertEqual(
                    rolling_hash.is_palindrome(le, ri),
                    s[le:ri] == s[le:ri][::-1],
                )

    def test_empty_and_non_lowercase_string(self):
        empty = self.RollingHash('', base=137)
        self.assertEqual(empty.get_hash(0, 0), 0)
        self.assertTrue(empty.is_palindrome(0, 0))

        s = 'AtCoder-123'
        rolling_hash = self.RollingHash(s, base=137)
        self.assertTrue(rolling_hash.equal(0, 2, 0, 2))
        self.assertEqual(rolling_hash.lcp(0, 2), 0)

    def test_segment_tree_hash_matches_rolling_hash(self):
        s = 'abacabadabacaba'
        rolling_hash = self.RollingHash(s, base=137)
        seg_hash = self.SegRollingHash(s, base=137)
        for le in range(len(s) + 1):
            for ri in range(le, len(s) + 1):
                forward = seg_hash.get_hash(le, ri)
                reverse = seg_hash.get_reverse_hash(le, ri)
                self.assertEqual(forward, rolling_hash.get_hash(le, ri))
                self.assertEqual(forward == reverse, s[le:ri] == s[le:ri][::-1])

    def test_update(self):
        s = list('abcba')
        rolling_hash = self.SegRollingHash(''.join(s), base=137)
        self.assertTrue(rolling_hash.is_palindrome(0, 5))
        rolling_hash.set(0, 'z')
        s[0] = 'z'
        self.assertFalse(rolling_hash.is_palindrome(0, 5))
        rolling_hash.set(4, 'z')
        s[4] = 'z'
        self.assertTrue(rolling_hash.is_palindrome(0, 5))

    def test_segment_tree_features_after_updates(self):
        s = list('abacabadabacaba')
        rolling_hash = self.SegRollingHash(''.join(s), base=137)
        for p, c in ((0, 'z'), (7, 'z'), (14, 'z'), (3, 'A')):
            rolling_hash.set(p, c)
            s[p] = c
            text = ''.join(s)
            expected_hash = self.RollingHash(text, base=137)
            for le in range(len(s) + 1):
                for ri in range(le, len(s) + 1):
                    self.assertEqual(
                        rolling_hash.get_hash(le, ri),
                        expected_hash.get_hash(le, ri),
                    )
                    self.assertEqual(
                        rolling_hash.get_reverse_hash(le, ri),
                        expected_hash.get_reverse_hash(le, ri),
                    )
                    self.assertEqual(
                        rolling_hash.is_palindrome(le, ri),
                        text[le:ri] == text[le:ri][::-1],
                    )
            for i in range(len(s) + 1):
                for j in range(len(s) + 1):
                    self.assertEqual(rolling_hash.lcp(i, j), expected_hash.lcp(i, j))


if __name__ == '__main__':
    unittest.main()
