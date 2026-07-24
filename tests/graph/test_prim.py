import unittest

from graph.prim import prim


class TestPrim(unittest.TestCase):
    def test_minimum_spanning_tree(self):
        cost = [
            [0, 1, 4, 3],
            [1, 0, 2, 5],
            [4, 2, 0, 1],
            [3, 5, 1, 0],
        ]
        to = prim(cost)

        edges = []
        for u in range(len(to)):
            for v, w in to[u]:
                if u < v:
                    edges.append((u, v, w))

        self.assertEqual(len(edges), 3)
        self.assertEqual(sum(w for _, _, w in edges), 4)
        self.assertEqual(
            {frozenset((u, v)) for u, v, _ in edges},
            {frozenset((0, 1)), frozenset((1, 2)), frozenset((2, 3))},
        )

    def test_single_vertex(self):
        self.assertEqual(prim([[0]]), [[]])

    def test_disconnected_graph(self):
        inf = 1 << 62
        with self.assertRaises(AssertionError):
            prim([
                [0, 1, inf],
                [1, 0, inf],
                [inf, inf, 0],
            ])


if __name__ == '__main__':
    unittest.main()
