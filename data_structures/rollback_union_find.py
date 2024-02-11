class RollbackUnionFind:
    def __init__(self, n):
        self._n = n
        self._root_or_size = [-1 for _ in range(n)]
        self._history = []

    def find(self, i):
        while self._root_or_size[i] >= 0:
            i = self._root_or_size[i]
        return i

    def unite(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri == rj:
            self._history.append((ri, -1, -1, -1))
            return ri
        if -self._root_or_size[ri] < -self._root_or_size[rj]:
            ri, rj = rj, ri
        self._history.append((ri, rj, self._root_or_size[ri], self._root_or_size[rj]))
        self._root_or_size[ri] += self._root_or_size[rj]
        self._root_or_size[rj] = ri
        return ri

    def same(self, i, j):
        return self.find(i) == self.find(j)

    def size(self, i):
        return -self._root_or_size[self.find(i)]

    def groups(self):
        result = [[] for _ in range(self._n)]
        for i in range(self._n):
            result[self.find(i)].append(i)
        return [x for x in result if x]

    def rollback(self):
        if not self._history:
            return False
        ri, rj, di, dj = self._history.pop()
        if rj == -1:
            return False
        self._root_or_size[ri] = di
        self._root_or_size[rj] = dj
        return True
