from itertools import product
import unittest

from tests.string._loader import load_string_module


class TestManacher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.Manacher = load_string_module('manacher')['Manacher']

    def test_judge_matches_naive_palindrome_check(self):
        for n in range(7):
            for chars in product('ab', repeat=n):
                s = ''.join(chars)
                manacher = self.Manacher(s)
                for le in range(n + 1):
                    for ri in range(le, n + 1):
                        expected = s[le:ri] == s[le:ri][::-1]
                        self.assertEqual(manacher.judge(le, ri), expected)
                        self.assertEqual(manacher.is_palindrome(le, ri), expected)

    def test_max_length(self):
        cases = {
            '': 0,
            'a': 1,
            'ab': 1,
            'abba': 4,
            'abacaba': 7,
            'abac': 3,
        }
        for s, expected in cases.items():
            with self.subTest(s=s):
                manacher = self.Manacher(s)
                self.assertEqual(manacher.max_length(), expected)
                self.assertEqual(manacher.longest_length(), expected)
                le, ri = manacher.longest_range()
                self.assertEqual(ri - le, expected)
                self.assertEqual(manacher.longest_palindrome(), s[le:ri])
                self.assertEqual(s[le:ri], s[le:ri][::-1])

    def test_all_longest_palindromes(self):
        manacher = self.Manacher('abacdc')
        self.assertEqual(manacher.longest_range(), (0, 3))
        self.assertEqual(manacher.longest_palindrome(), 'aba')
        self.assertEqual(manacher.longest_ranges(), [(0, 3), (3, 6)])
        self.assertEqual(manacher.longest_palindromes(), ['aba', 'cdc'])

        empty = self.Manacher('')
        self.assertEqual(empty.longest_ranges(), [(0, 0)])
        self.assertEqual(empty.longest_palindromes(), [''])

    def test_count_matches_naive_count(self):
        for n in range(7):
            for chars in product('ab', repeat=n):
                s = ''.join(chars)
                expected = sum(
                    s[le:ri] == s[le:ri][::-1]
                    for le in range(n)
                    for ri in range(le + 1, n + 1)
                )
                self.assertEqual(self.Manacher(s).count(), expected)

    def test_center_lengths(self):
        for n in range(7):
            for chars in product('ab', repeat=n):
                s = ''.join(chars)
                expected = [0 for _ in range(2 * n + 1)]
                for le in range(n + 1):
                    for ri in range(le, n + 1):
                        if s[le:ri] == s[le:ri][::-1]:
                            expected[le + ri] = max(expected[le + ri], ri - le)
                self.assertEqual(self.Manacher(s).center_lengths(), expected)

    def test_sequence(self):
        manacher = self.Manacher([1, 2, 3, 2, 1])
        self.assertTrue(manacher.judge(0, 5))
        self.assertFalse(manacher.judge(0, 4))
        self.assertEqual(manacher.longest_palindrome(), [1, 2, 3, 2, 1])


if __name__ == '__main__':
    unittest.main()
