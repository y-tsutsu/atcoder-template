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
                self.assertEqual(self.Manacher(s).max_length(), expected)

    def test_sequence(self):
        manacher = self.Manacher([1, 2, 3, 2, 1])
        self.assertTrue(manacher.judge(0, 5))
        self.assertFalse(manacher.judge(0, 4))


if __name__ == '__main__':
    unittest.main()
