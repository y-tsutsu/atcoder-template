import unittest

from graph.functional_graph import find_cycle as find_functional_cycles
from tests.graph._loader import load_graph_module


class TestConnectivityAndFlow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maximum_flow = load_graph_module('maximum_flow')
        cls.Dinic = cls.maximum_flow['Dinic']
        cls.hopcroft_karp = load_graph_module('hopcroft_karp')
        cls.bipartite_matching = load_graph_module('bipartite_matching', Dinic=cls.Dinic)
        cls.scc_module = load_graph_module('scc')
        cls.find_cycle_module = load_graph_module('find_cycle')

    def test_dinic(self):
        flow = self.Dinic(4)
        for edge in [(0, 1, 2), (0, 2, 1), (1, 2, 1), (1, 3, 1), (2, 3, 2)]:
            flow.add_edge(*edge)
        self.assertEqual(flow.flow(0, 3), 3)
        with self.assertRaises(AssertionError):
            self.Dinic(1).flow(0, 0)

    def test_bipartite_matching(self):
        matching = self.bipartite_matching['BpMatch'](3, 3)
        for edge in [(0, 0), (0, 1), (1, 1), (2, 2)]:
            matching.add_edge(*edge)
        self.assertEqual(matching.flow(), 3)

    def test_hopcroft_karp(self):
        matching = self.hopcroft_karp['HopcroftKarp'](3, 3)
        for edge in [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]:
            matching.add_edge(*edge)
        self.assertEqual(matching.flow(), 3)

    def test_scc(self):
        edges = [(0, 1), (1, 0), (1, 2), (2, 3), (3, 2), (3, 4)]
        scc = self.scc_module['SCC'](5)
        for u, v in edges:
            scc.add_edge(u, v)
        self.assertEqual(scc.build(), 3)
        self.assertEqual(scc.label, [0, 0, 1, 1, 2])
        self.assertEqual(scc.groups(), [[0, 1], [2, 3], [4]])
        self.assertEqual(scc.dag(), [[1], [2], []])
        self.assertTrue(scc.same(0, 1))
        self.assertFalse(scc.same(1, 2))

    def test_scc_with_isolated_vertex_and_duplicate_edges(self):
        scc = self.scc_module['SCC'](4)
        for edge in ((0, 0), (0, 1), (0, 1), (1, 0), (1, 2)):
            scc.add_edge(*edge)
        self.assertEqual(scc.build(), 3)
        self.assertEqual(scc.groups(), [[3], [0, 1], [2]])
        self.assertEqual(scc.dag(), [[], [2], []])

    def test_scc_without_recursion(self):
        n = 10000
        scc = self.scc_module['SCC'](n)
        for i in range(n - 1):
            scc.add_edge(i, i + 1)
        self.assertEqual(scc.build(), n)
        self.assertEqual(scc.label, list(range(n)))

    def test_directed_cycle(self):
        find_cycle = self.find_cycle_module['find_cycle']
        has_cycle = self.find_cycle_module['has_cycle']
        self.assertEqual(find_cycle(3, [[1], [2], [0]]), [0, 1, 2])
        self.assertEqual(find_cycle(3, [[1], [2], []]), [])
        self.assertTrue(has_cycle(3, [[1], [2], [0]]))
        self.assertFalse(has_cycle(3, [[1], [2], []]))

    def test_directed_cycle_with_self_loop(self):
        find_cycle = self.find_cycle_module['find_cycle']
        self.assertEqual(find_cycle(3, [[], [1], []]), [1])

    def test_directed_cycle_in_disconnected_graph(self):
        find_cycle = self.find_cycle_module['find_cycle']
        to = [[1], [], [3], [4], [2]]
        cycle = find_cycle(5, to)
        self.assertEqual(set(cycle), {2, 3, 4})
        for v, u in zip(cycle, cycle[1:] + cycle[:1]):
            self.assertIn(u, to[v])

    def test_directed_cycle_without_recursion(self):
        find_cycle = self.find_cycle_module['find_cycle']
        n = 10000
        to = [[i + 1] for i in range(n - 1)] + [[0]]
        self.assertEqual(find_cycle(n, to), list(range(n)))

    def test_functional_graph_cycles(self):
        self.assertEqual(find_functional_cycles(7, [1, 2, 0, 4, 3, 2, 5]), [[0, 1, 2], [3, 4]])


if __name__ == '__main__':
    unittest.main()
