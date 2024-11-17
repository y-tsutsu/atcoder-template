class MonoidUnionFind:
    def __init__(self, n, data, op, values=None):
        self._n = n
        self._root_or_size = [-1 for _ in range(n)]
        self._count = n
        self._data = data
        self._op = op
        if values is None:
            self._values = [i for i in range(n)]
        else:
            self._values = values

    def find(self, i):
        if self._root_or_size[i] < 0:
            return i
        self._root_or_size[i] = self.find(self._root_or_size[i])
        return self._root_or_size[i]

    def unite(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri == rj:
            return ri
        self._count -= 1
        if -self._root_or_size[ri] < -self._root_or_size[rj]:
            ri, rj = rj, ri
        self._root_or_size[ri] += self._root_or_size[rj]
        self._root_or_size[rj] = ri
        self._data[ri] = self._op(self._data[ri], self._data[rj])
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

    def count(self):
        return self._count

    def data(self, i):
        return self._data[self.find(i)]

    def value(self, i):
        return self._values[self.find(i)]

    def set_value(self, i, value):
        self._values[self.find(i)] = value
