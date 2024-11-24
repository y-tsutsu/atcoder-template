class WeightedUnionFind:
    def __init__(self, n):
        self._n = n
        self._par = [i for i in range(n)]
        self._rank = [0 for _ in range(n)]
        self._weight = [0 for _ in range(n)]

    def find(self, i):
        if self._par[i] == i:
            return i
        y = self.find(self._par[i])
        self._weight[i] += self._weight[self._par[i]]
        self._par[i] = y
        return y

    def unite(self, i, j, w):
        rx = self.find(i)
        ry = self.find(j)
        if self._rank[rx] < self._rank[ry]:
            self._par[rx] = ry
            self._weight[rx] = w - self._weight[i] + self._weight[j]
        else:
            self._par[ry] = rx
            self._weight[ry] = -w - self._weight[j] + self._weight[i]
            if self._rank[rx] == self._rank[ry]:
                self._rank[rx] += 1

    def same(self, i, j):
        return self.find(i) == self.find(j)

    def diff(self, i, j):
        if not self.same(i, j):
            return None
        return self._weight[i] - self._weight[j]

    def groups(self):
        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[self.find(i)].append(i)
        return [x for x in result if x]
