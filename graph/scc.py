def recurboost(func=None, stack=[]):
    pass


class SCC:
    '''強連結成分（Strongly Connected Components）'''

    def __init__(self, n, to, ot):
        self._n = n
        self._to = to
        self._ot = ot
        self._order = []
        self._group = [None for _ in range(n)]

    @recurboost(stack=[])
    def dfs(self, s, to, used):
        used[s] = 1
        for i in to[s]:
            if not used[i]:
                yield self.dfs(i, to, used)
        self._order.append(s)
        yield

    @recurboost(stack=[])
    def rdfs(self, s, to, label, used):
        self._group[s] = label
        used[s] = 1
        for i in to[s]:
            if not used[i]:
                yield self.rdfs(i, to, label, used)
        yield

    def _construct(self, n, to, label):
        p = [[] for _ in range(label)]
        q = [set() for _ in range(label)]
        for i in range(n):
            u = self._group[i]
            for w in to[i]:
                v = self._group[w]
                if u == v:
                    continue
                q[u].add(v)
            p[u].append(i)
        return p, q

    def scc(self):
        '''各グループ毎の頂点リストと，グループ単位での遷移先'''
        used = [0 for _ in range(self._n)]
        for i in range(self._n):
            if not used[i]:
                self.dfs(i, self._to, used)
        label = 0
        rused = [0 for _ in range(self._n)]
        for s in reversed(self._order):
            if not rused[s]:
                self.rdfs(s, self._ot, label, rused)
                label += 1
        return self._construct(self._n, self._to, label)


def example():
    n = 10
    e = [(0, 1), (0, 2), (1, 4), (2, 0), (2, 6), (2, 8), (3, 1), (3, 5),
         (4, 3), (4, 7), (5, 3), (6, 7), (6, 8), (7, 3), (7, 9), (8, 6), (8, 7)]
    to = [[] for _ in range(n)]
    ot = [[] for _ in range(n)]
    for u, v in e:
        to[u].append(v)
        ot[v].append(u)
    scc = SCC(n, to, ot)
    p, q = scc.scc()
    print(p, q)


if __name__ == '__main__':
    example()
