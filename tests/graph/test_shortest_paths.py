import unittest

from graph.bellman_ford import INF as BELLMAN_FORD_INF
from graph.bellman_ford import bellman_ford
from graph.bellman_ford import check_reachable
from graph.warshall_floyd import INF
from graph.warshall_floyd import exist_negative_cycle
from graph.warshall_floyd import is_disconnected_vertex
from graph.warshall_floyd import update_new_edge
from graph.warshall_floyd import warshall_floyd


class TestShortestPaths(unittest.TestCase):
    def test_bellman_ford(self):
        edges = [(0, 1, 2), (0, 2, 5), (1, 2, -1), (2, 3, 2)]
        distance = [BELLMAN_FORD_INF] * 4
        distance[0] = 0
        self.assertTrue(bellman_ford(4, distance, edges))
        self.assertEqual(distance, [0, 2, 1, 3])

    def test_bellman_ford_negative_cycle(self):
        edges = [(0, 1, 1), (1, 2, -2), (2, 1, 1), (2, 3, 1)]
        distance = [BELLMAN_FORD_INF] * 4
        distance[0] = 0
        self.assertFalse(bellman_ford(4, distance, edges))
        self.assertEqual(distance[1:], [-BELLMAN_FORD_INF] * 3)

    def test_check_reachable(self):
        to = [[1, 3], [2], [], [4], []]
        reverse = [[], [0], [1], [0], [3]]
        self.assertEqual(check_reachable(5, to, reverse), [1, 0, 0, 1, 1])

    def test_warshall_floyd(self):
        d = [[INF] * 4 for _ in range(4)]
        for i in range(4):
            d[i][i] = 0
        for u, v, w in [(0, 1, 2), (1, 2, -1), (0, 2, 5)]:
            d[u][v] = w
        warshall_floyd(4, d)
        self.assertEqual(d[0][2], 1)
        self.assertTrue(is_disconnected_vertex(d, 0, 3))
        self.assertFalse(exist_negative_cycle(4, d))

    def test_update_new_edge(self):
        d = [[0, 5, 9], [5, 0, 4], [9, 4, 0]]
        update_new_edge(3, d, 0, 2, 2)
        self.assertEqual(d, [[0, 5, 2], [5, 0, 4], [2, 4, 0]])


if __name__ == '__main__':
    unittest.main()
