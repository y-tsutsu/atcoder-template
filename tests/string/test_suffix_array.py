from itertools import product
import unittest

from tests.string._loader import load_string_module


class TestSuffixArray(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manber_myers = staticmethod(load_string_module('suffix_array')['manber_myers'])

    def test_matches_naive_suffix_sort(self):
        for n in range(7):
            for chars in product('abc', repeat=n):
                s = ''.join(chars)
                expected = sorted(range(n + 1), key=lambda i: s[i:])
                self.assertEqual(self.manber_myers(s), expected)

    def test_custom_conversion(self):
        a = [30, 10, 20, 10]
        expected = sorted(range(len(a) + 1), key=lambda i: a[i:])
        self.assertEqual(self.manber_myers(a, conv=lambda x: x), expected)


if __name__ == '__main__':
    unittest.main()
