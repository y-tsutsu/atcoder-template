def bootstrap(func=None, stack=[]):
    pass


class LCA:
    def __init__(self, n):
        assert n > 0
        self._n = n
        self._LOG = max(1, (n - 1).bit_length())
        self._to = [[] for _ in range(n)]
        self._parent = [[-1 for _ in range(n)] for _ in range(self._LOG)]
        self._depth = [0 for _ in range(n)]
        self._dist = [0 for _ in range(n)]

    @bootstrap
    def _dfs(self, v, p, d, dist):
        self._parent[0][v] = p
        self._depth[v] = d
        self._dist[v] = dist
        for nv, w in self._to[v]:
            if nv == p:
                continue
            yield self._dfs(nv, v, d + 1, dist + w)
        yield

    def add_edge(self, u, v, w=1):
        self._to[u].append((v, w))
        self._to[v].append((u, w))

    def build(self, root=0):
        self._dfs(root, -1, 0, 0)
        for k in range(self._LOG - 1):
            for v in range(self._n):
                if self._parent[k][v] < 0:
                    self._parent[k + 1][v] = -1
                else:
                    self._parent[k + 1][v] = self._parent[k][self._parent[k][v]]

    def lca(self, u, v):
        if self._depth[u] < self._depth[v]:
            u, v = v, u
        diff = self._depth[u] - self._depth[v]
        for k in range(self._LOG):
            if diff >> k & 1:
                u = self._parent[k][u]
        if u == v:
            return u
        for k in reversed(range(self._LOG)):
            if self._parent[k][u] != self._parent[k][v]:
                u = self._parent[k][u]
                v = self._parent[k][v]
        return self._parent[0][u]

    def distance(self, u, v):
        x = self.lca(u, v)
        return self._dist[u] + self._dist[v] - 2 * self._dist[x]

    def kth_ancestor(self, v, k):
        '''vのk個上の祖先'''
        if k < 0 or self._depth[v] < k:
            return -1
        for i in range(self._LOG):
            if v < 0:
                return -1
            if k >> i & 1:
                v = self._parent[i][v]
        return v

    def kth_node(self, u, v, k):
        '''u -> vのパス上でk番目のノード'''
        x = self.lca(u, v)
        d1 = self._depth[u] - self._depth[x]
        d2 = self._depth[v] - self._depth[x]
        if k < 0 or d1 + d2 < k:
            return -1
        if k <= d1:
            return self.kth_ancestor(u, k)
        else:
            k2 = d2 - (k - d1)
            return self.kth_ancestor(v, k2)
