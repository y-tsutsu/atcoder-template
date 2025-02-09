class BIT:
    def __init__(self, n):
        self._n = n
        self._d = [0 for _ in range(n)]

    def add(self, p, x):
        p += 1
        while p <= self._n:
            self._d[p - 1] += x
            p += p & -p

    def sum(self, s, e):
        '''[s, e)'''
        return self._sum(e) - self._sum(s)

    def _sum(self, e):
        '''[0, e)'''
        s = 0
        while e > 0:
            s += self._d[e - 1]
            e -= e & -e
        return s

    def get(self, p):
        return self.sum(p, p + 1)

    def set(self, p, x):
        y = self.get(p)
        self.add(p, x - y)


class BITAddRange:
    '''区間加算用BIT'''

    def __init__(self, n):
        self._bit = BIT(n + 1)

    def add(self, s, e, x):
        '''[s, e)'''
        self._bit.add(s, x)
        self._bit.add(e, -x)

    def get(self, p):
        return self._bit.sum(0, p + 1)


def bisect_ng_ok(s, e, is_ok):
    pass


class BITSortedMultiset:
    def __init__(self, max_):
        self._max = max_
        self._size = 0
        self._bit = BIT(self._max + 1)

    def __len__(self):
        return self._size

    def __str__(self):
        p = []
        for i in range(self._max + 1):
            p += [i for _ in range(self._bit.get(i))]
        return str(p)

    def __contains__(self, x):
        assert x <= self._max
        return self._bit.get(x) != 0

    def __getitem__(self, i):
        def f(i):
            def _f(x):
                tot = self._bit.sum(0, x + 1)
                return tot >= i + 1
            return _f
        if self._size <= i:
            return None
        return bisect_ng_ok(0, self._max, f(i))

    def add(self, x):
        assert x <= self._max
        self._bit.add(x, 1)
        self._size += 1

    def discard(self, x):
        assert x <= self._max
        if self._bit.get(x) == 0:
            return
        self._bit.add(x, -1)
        self._size -= 1
