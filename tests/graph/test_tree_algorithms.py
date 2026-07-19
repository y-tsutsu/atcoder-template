import unittest

from graph.rerooting import Rerooting
from tests.graph._loader import load_graph_module


class TestTreeAlgorithms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.lca_module = load_graph_module('lca')
        cls.cartesian_tree_module = load_graph_module('cartesian_tree')
        cls.tree_diameter_module = load_graph_module('tree_diameter')

    def test_lca(self):
        lca = self.lca_module['LCA'](6)
        for u, v, w in [(0, 1, 2), (0, 2, 3), (1, 3, 4), (1, 4, 5), (2, 5, 6)]:
            lca.add_edge(u, v, w)
        lca.build()
        self.assertEqual(lca.lca(3, 4), 1)
        self.assertEqual(lca.lca(3, 5), 0)
        self.assertEqual(lca.distance(3, 5), 15)
        self.assertEqual(lca.kth_ancestor(3, 2), 0)
        self.assertEqual(lca.kth_ancestor(3, 3), -1)
        self.assertEqual([lca.kth_node(3, 5, k) for k in range(5)], [3, 1, 0, 2, 5])
        self.assertEqual(lca.kth_node(3, 5, 5), -1)

    def test_lca_single_vertex(self):
        lca = self.lca_module['LCA'](1)
        lca.build()
        self.assertEqual(lca.lca(0, 0), 0)
        self.assertEqual(lca.distance(0, 0), 0)

    def test_cartesian_tree(self):
        cartesian_tree = self.cartesian_tree_module['cartesian_tree']
        self.assertEqual(cartesian_tree(3, [10, 30, 20]), [[], [0, 2], []])
        with self.assertRaises(AssertionError):
            cartesian_tree(3, [1, 1, 2])

    def test_tree_diameter_and_route(self):
        to = [[(1, 2)], [(0, 2), (2, 3), (3, 4)], [(1, 3)], [(1, 4)]]
        diameter = self.tree_diameter_module['diameter']
        route = self.tree_diameter_module['route']
        s, e, distance = diameter(4, to)
        self.assertEqual(distance, 7)
        self.assertEqual(route(s, e, to), [s, 1, e])

    def test_rerooting(self):
        rerooting = Rerooting(
            4,
            (0, 0),
            lambda x, y: (x[0] + y[0], x[1] + y[1]),
            lambda x, v: (x[0], x[1] + 1),
            lambda x, data: (x[0] + x[1], x[1]),
        )
        for u, v in [(0, 1), (1, 2), (1, 3)]:
            rerooting.add(u, v)
        self.assertEqual([x for x, _ in rerooting.solve()], [5, 3, 5, 5])


if __name__ == '__main__':
    unittest.main()
