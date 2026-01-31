from collections import deque
from sys import maxsize


def recurboost(func=None, stack=[]):
    pass


class HopcroftKarp:
    '''最大二部マッチング'''

    def __init__(self, nl, nr):
        self._nl = nl
        self._nr = nr
        self._g = [[] for _ in range(nl)]
        self._matchl = [-1 for _ in range(nl)]
        self._matchr = [-1 for _ in range(nr)]
        self._dist = [0 for _ in range(nl)]

    def add_edge(self, u, v):
        self._g[u].append(v)

    def _bfs(self):
        dq = deque()
        INF = maxsize

        for i in range(self._nl):
            if self._matchl[i] == -1:
                self._dist[i] = 0
                dq.append(i)
            else:
                self._dist[i] = INF

        found = False
        while dq:
            v = dq.popleft()
            for w in self._g[v]:
                u = self._matchr[w]
                if u == -1:
                    found = True
                elif self._dist[u] == INF:
                    self._dist[u] = self._dist[v] + 1
                    dq.append(u)

        return found

    @recurboost
    def _dfs(self, v):
        for w in self._g[v]:
            u = self._matchr[w]
            if u == -1 or (self._dist[u] == self._dist[v] + 1 and (yield self._dfs(u))):
                self._matchl[v] = w
                self._matchr[w] = v
                yield True
        INF = maxsize
        self._dist[v] = INF
        yield False

    def flow(self):
        ret = 0
        while self._bfs():
            for i in range(self._nl):
                if self._matchl[i] == -1 and self._dfs(i):
                    ret += 1
        return ret
