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
        to = [[] for _ in range(5)]
        reverse = [[] for _ in range(5)]
        for u, v in edges:
            to[u].append(v)
            reverse[v].append(u)
        groups, graph = self.scc_module['SCC'](5, to, reverse).scc()
        self.assertEqual(groups, [[0, 1], [2, 3], [4]])
        self.assertEqual(graph, [{1}, {2}, set()])

    def test_directed_cycle(self):
        find_cycle = self.find_cycle_module['find_cycle']
        self.assertTrue(find_cycle(3, [[1], [2], [0]]))
        self.assertFalse(find_cycle(3, [[1], [2], []]))

    def test_functional_graph_cycles(self):
        self.assertEqual(find_functional_cycles(7, [1, 2, 0, 4, 3, 2, 5]), [[0, 1, 2], [3, 4]])


if __name__ == '__main__':
    unittest.main()
