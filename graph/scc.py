class SCC:
    '''有向グラフを互いに行き来できる頂点集合へ分解する強連結成分分解

    build()後、label[v]は頂点vが属する成分番号になる。
    成分番号は縮約後のDAGにおけるトポロジカル順に付く。
    '''

    def __init__(self, n):
        self._n = n
        self._to = [[] for _ in range(n)]
        self._reverse = [[] for _ in range(n)]
        self._built = False
        self.label = [-1 for _ in range(n)]
        self._groups = []
        self._dag = []

    def add_edge(self, u, v):
        '''有向辺u -> vを追加する'''
        assert not self._built
        self._to[u].append(v)
        self._reverse[v].append(u)

    def build(self):
        '''強連結成分分解を行い、成分数を返す'''
        assert not self._built
        self._built = True

        order = []
        used = [False for _ in range(self._n)]
        for start in range(self._n):
            if used[start]:
                continue
            used[start] = True
            stack = [(start, 0)]
            while stack:
                v, i = stack[-1]
                if i == len(self._to[v]):
                    order.append(v)
                    stack.pop()
                    continue
                u = self._to[v][i]
                stack[-1] = (v, i + 1)
                if not used[u]:
                    used[u] = True
                    stack.append((u, 0))

        for start in reversed(order):
            if self.label[start] >= 0:
                continue
            group_id = len(self._groups)
            group = []
            self.label[start] = group_id
            stack = [start]
            while stack:
                v = stack.pop()
                group.append(v)
                for u in self._reverse[v]:
                    if self.label[u] < 0:
                        self.label[u] = group_id
                        stack.append(u)
            self._groups.append(sorted(group))

        edges = [set() for _ in self._groups]
        for v in range(self._n):
            for u in self._to[v]:
                if self.label[v] != self.label[u]:
                    edges[self.label[v]].add(self.label[u])
        self._dag = [sorted(edge) for edge in edges]
        return len(self._groups)

    def same(self, u, v):
        '''uとvが同じ強連結成分に属するかを返す'''
        assert self._built
        return self.label[u] == self.label[v]

    def groups(self):
        '''各強連結成分に属する頂点一覧を返す'''
        assert self._built
        return self._groups

    def dag(self):
        '''各強連結成分を1頂点へ縮約したDAGを返す'''
        assert self._built
        return self._dag


def example():
    # 0 -> 1 -> 2 -> 0 と 3 <-> 4 がそれぞれ強連結成分になる
    edges = [
        (0, 1), (1, 2), (2, 0),
        (2, 3),
        (3, 4), (4, 3),
        (4, 5),
    ]
    scc = SCC(6)
    for u, v in edges:
        scc.add_edge(u, v)

    print(scc.build())     # 3: 強連結成分の個数
    print(scc.label)       # [0, 0, 0, 1, 1, 2]
    print(scc.groups())    # [[0, 1, 2], [3, 4], [5]]
    print(scc.same(0, 2))  # True: 互いに行き来できる
    print(scc.same(0, 3))  # False

    # 成分0 -> 成分1 -> 成分2というDAGへ縮約される
    print(scc.dag())       # [[1], [2], []]


if __name__ == '__main__':
    example()
