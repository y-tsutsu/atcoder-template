from itertools import product
import unittest

from tests.string._loader import load_string_module


class TestSuffixArray(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        module = load_string_module('suffix_array')
        cls.SuffixArray = module['SuffixArray']
        cls.longest_common_substring = staticmethod(module['longest_common_substring'])

    def test_suffix_array_matches_naive_sort(self):
        for n in range(7):
            for chars in product('abc', repeat=n):
                s = ''.join(chars)
                suffix_array = self.SuffixArray(s)
                expected = sorted(range(n), key=lambda i: s[i:])
                self.assertEqual(suffix_array.sa, expected)
                self.assertEqual(len(suffix_array), n)
                self.assertEqual(
                    [suffix_array[i] for i in range(n)],
                    expected,
                )

    def test_lcp_array_matches_naive_comparison(self):
        for s in ('', 'a', 'aaaaa', 'banana', 'mississippi', 'abracadabra'):
            suffix_array = self.SuffixArray(s)
            expected = []
            for i, j in zip(suffix_array.sa, suffix_array.sa[1:]):
                length = 0
                while i + length < len(s) and j + length < len(s):
                    if s[i + length] != s[j + length]:
                        break
                    length += 1
                expected.append(length)
            self.assertEqual(suffix_array.lcp, expected)

    def test_lcp_suffix_matches_naive_comparison(self):
        for s in ('a', 'aaaaa', 'banana', 'mississippi'):
            suffix_array = self.SuffixArray(s)
            for i in range(len(s)):
                for j in range(len(s)):
                    expected = 0
                    while i + expected < len(s) and j + expected < len(s):
                        if s[i + expected] != s[j + expected]:
                            break
                        expected += 1
                    self.assertEqual(suffix_array.lcp_suffix(i, j), expected)

    def test_search_matches_naive_search(self):
        for s in ('banana', 'aaaaa', 'abracadabra'):
            suffix_array = self.SuffixArray(s)
            for length in range(1, 4):
                for chars in product('abc', repeat=length):
                    pattern = ''.join(chars)
                    positions = [
                        i for i in range(len(s))
                        if s.startswith(pattern, i)
                    ]
                    le, ri = suffix_array.search(pattern)
                    self.assertEqual(ri - le, len(positions))
                    self.assertEqual(suffix_array.contains(pattern), bool(positions))
                    self.assertEqual(suffix_array.count(pattern), len(positions))
                    self.assertEqual(suffix_array.positions(pattern), positions)
                    self.assertTrue(all(s[i:].startswith(pattern) for i in suffix_array.sa[le:ri]))

    def test_distinct_substrings(self):
        for n in range(7):
            for chars in product('ab', repeat=n):
                s = ''.join(chars)
                expected = len({s[le:ri] for le in range(n) for ri in range(le + 1, n + 1)})
                self.assertEqual(self.SuffixArray(s).distinct_substrings(), expected)

    def test_longest_repeated_substring(self):
        self.assertEqual(self.SuffixArray('').longest_repeated_substring(), '')
        self.assertEqual(self.SuffixArray('abc').longest_repeated_substring(), '')
        self.assertEqual(self.SuffixArray('banana').longest_repeated_substring(), 'ana')
        self.assertEqual(self.SuffixArray('aaaaa').longest_repeated_substring(), 'aaaa')

    def test_longest_common_substring(self):
        self.assertEqual(self.longest_common_substring('abcde', 'cdef'), 'cde')
        self.assertEqual(self.longest_common_substring('banana', 'ananas'), 'anana')
        self.assertEqual(self.longest_common_substring('abc', 'xyz'), '')
        self.assertEqual(self.longest_common_substring('', 'abc'), '')

        s, t = 'ababa', 'babab'
        actual = self.longest_common_substring(s, t)
        expected_length = max(
            (len(s[le:ri]) for le in range(len(s)) for ri in range(le + 1, len(s) + 1)
             if s[le:ri] in t),
            default=0,
        )
        self.assertEqual(len(actual), expected_length)
        self.assertIn(actual, s)
        self.assertIn(actual, t)


if __name__ == '__main__':
    unittest.main()
