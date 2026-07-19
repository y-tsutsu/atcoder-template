import unittest

from bootstrap.bootstrapmemo import bootstrapmemo


class TestBootstrapMemo(unittest.TestCase):
    def test_dict_memo(self):
        memo = {}

        @bootstrapmemo(stack=[], memo=memo, args_list=[])
        def fibonacci(n):
            if n < 2:
                yield n
            yield (yield fibonacci(n - 1)) + (yield fibonacci(n - 2))

        self.assertEqual(fibonacci(100), 354224848179261915075)
        self.assertEqual(fibonacci(100), 354224848179261915075)
        self.assertEqual(len(memo), 101)

    def test_2d_list_memo(self):
        memo = [[None for _ in range(6)] for _ in range(6)]

        @bootstrapmemo(stack=[], memo=memo, args_list=[])
        def paths(i, j):
            if i == 0 or j == 0:
                yield 1
            yield (yield paths(i - 1, j)) + (yield paths(i, j - 1))

        self.assertEqual(paths(5, 5), 252)
        self.assertEqual(memo[5][5], 252)


if __name__ == '__main__':
    unittest.main()
