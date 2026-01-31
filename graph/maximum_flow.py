from collections import deque
from sys import maxsize


def recurboost(func=None, stack=[]):
    pass


class Dinic:
    '''Dinic's Algorithm'''

    def __init__(self, n):
        self._n = n
        self._to = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        forward = [to, cap, None]
        forward[2] = backward = [fr, 0, forward]
        self._to[fr].append(forward)
        self._to[to].append(backward)

    def add_multi_edge(self, v1, v2, cap1, cap2):
        edge1 = [v2, cap1, None]
        edge1[2] = edge2 = [v1, cap2, edge1]
        self._to[v1].append(edge1)
        self._to[v2].append(edge2)

    def _bfs(self, s, t):
        self._level = level = [None] * self._n
        dq = deque([s])
        level[s] = 0
        while dq:
            v = dq.popleft()
            lv = level[v] + 1
            for w, cap, _ in self._to[v]:
                if cap and level[w] is None:
                    level[w] = lv
                    dq.append(w)
        return level[t] is not None

    @recurboost
    def _dfs(self, v, t, f, it):
        if v == t:
            yield f
        level = self._level
        for e in it[v]:
            w, cap, rev = e
            if cap and level[v] < level[w]:
                d = yield self._dfs(w, t, min(f, cap), it)
                if d:
                    e[1] -= d
                    rev[1] += d
                    yield d
        yield 0

    def flow(self, s, t):
        flow = 0
        INF = maxsize
        while self._bfs(s, t):
            *it, = map(iter, self._to)
            f = INF
            while f:
                f = self._dfs(s, t, INF, it)
                flow += f
        return flow
