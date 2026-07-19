import unittest

from tests.math._loader import load_math_module


class TestRoundHalfUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        module = load_math_module('round_half_up')
        cls.round_half_up = staticmethod(module['round_half_up'])
        cls.round_half_up_float = staticmethod(module['round_half_up_float'])
        cls.round_half_up_float_simple = staticmethod(module['round_half_up_float_simple'])

    def test_integer(self):
        cases = [
            (123, 0, 123),
            (123, 1, 120),
            (125, 1, 130),
            (149, 2, 100),
            (150, 2, 200),
            (999, 3, 1000),
        ]
        for n, ndigits, expected in cases:
            self.assertEqual(self.round_half_up(n, ndigits), expected)

    def test_negative_integer(self):
        cases = [
            (-123, 1, -120),
            (-125, 1, -130),
            (-149, 2, -100),
            (-150, 2, -200),
        ]
        for n, ndigits, expected in cases:
            self.assertEqual(self.round_half_up(n, ndigits), expected)

    def test_integer_rejects_negative_ndigits(self):
        with self.assertRaises(AssertionError):
            self.round_half_up(123, -1)

    def test_float(self):
        cases = [
            (2.675, 2, 2.68),
            (1.5, 0, 2.0),
            (1.25, 1, 1.3),
            (123.45, 1, 123.5),
            (125.0, -1, 130.0),
        ]
        for n, ndigits, expected in cases:
            self.assertEqual(self.round_half_up_float(n, ndigits), expected)

    def test_negative_float(self):
        cases = [
            (-2.675, 2, -2.68),
            (-1.5, 0, -2.0),
            (-1.25, 1, -1.3),
            (-125.0, -1, -130.0),
        ]
        for n, ndigits, expected in cases:
            self.assertEqual(self.round_half_up_float(n, ndigits), expected)

    def test_simple_float(self):
        self.assertEqual(self.round_half_up_float_simple(2.675, 2), 2.68)
        self.assertEqual(self.round_half_up_float_simple(1.25, 1), 1.3)


if __name__ == '__main__':
    unittest.main()
