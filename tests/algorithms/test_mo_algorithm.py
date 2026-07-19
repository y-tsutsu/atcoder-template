import unittest

from algorithms.mo_algorithm import mo


class TestMoAlgorithm(unittest.TestCase):
    def test_query_order(self):
        queries = [(0, 3), (1, 5), (5, 8), (6, 7)]
        self.assertEqual(mo(queries, len(queries), 10), list(enumerate(queries)))

    def test_contains_every_query(self):
        queries = [(7, 9), (0, 4), (3, 8), (1, 2), (5, 6)]
        ordered = mo(queries, len(queries), 10)
        self.assertEqual(sorted(ordered), list(enumerate(queries)))


if __name__ == '__main__':
    unittest.main()
