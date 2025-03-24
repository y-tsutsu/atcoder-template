from collections import deque


class LCA:
    def __init__(self, n, to, root=0):
        self._m = (n - 1).bit_length()
        self._prv, self._depth = self._initialize(n, to, root)
        self._kprv = self._create_kprv(self._prv, n, self._m)

    def _initialize(self, n, to, root):
        prv = [None for _ in range(n)]
        depth = [-1 for _ in range(n)]
        depth[root] = 0
        dq = deque()
        dq.append(root)
        while dq:
            i = dq.popleft()
            for j in to[i]:
                if depth[j] != -1:
                    continue
                prv[j] = i
                to[j].remove(i)
                depth[j] = depth[i] + 1
                dq.append(j)
        return prv, depth

    def _create_kprv(self, prv, n, m):
        kprv = [prv]
        p = prv
        for _ in range(m):
            q = [0 for _ in range(n)]
            for i in range(n):
                if p[i] is None:
                    continue
                q[i] = p[p[i]]
            kprv.append(q)
            p = q
        return kprv

    def lca(self, u, v):
        dd = self._depth[v] - self._depth[u]
        if dd < 0:
            u, v = v, u
            dd = -dd
        for k in range(self._m + 1):
            if dd & 1:
                v = self._kprv[k][v]
            dd >>= 1
        if u == v:
            return u
        for k in range(self._m - 1, -1, -1):
            pu = self._kprv[k][u]
            pv = self._kprv[k][v]
            if pu != pv:
                u = pu
                v = pv
        return self._kprv[0][u]

    def distance(self, u, v):
        lca = self.lca(u, v)
        return self._depth[u] + self._depth[v] - 2 * self._depth[lca]
