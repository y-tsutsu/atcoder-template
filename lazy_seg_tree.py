class LazySegTreeRAQ:
    '''区間加算用'''

    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << (n-1).bit_length()
        self._d = [self._e()] * (self._size << 1)
        self._lazy = [0] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def _gindex(self, s, e):
        s += self._size
        e += self._size
        lm = s >> (s & -s).bit_length()
        rm = e >> (e & -e).bit_length()
        while e > s:
            if s <= lm:
                yield s
            if e <= rm:
                yield e
            e >>= 1
            s >>= 1
        while s:
            yield s
            s >>= 1

    def _propagates(self, *ids):
        for i in reversed(ids):
            v = self._lazy[i]
            if v == 0:
                continue
            self._lazy[i] = 0
            self._lazy[i << 1] += v
            self._lazy[i << 1 | 1] += v
            self._d[i << 1] += v
            self._d[i << 1 | 1] += v

    def add(self, s, e, x):
        '''[s, e)'''
        ids = self._gindex(s, e)
        s += self._size
        e += self._size
        while s < e:
            if s & 1:
                self._lazy[s] += x
                self._d[s] += x
                s += 1
            if e & 1:
                self._lazy[e - 1] += x
                self._d[e - 1] += x
            e >>= 1
            s >>= 1
        for i in ids:
            self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1]) + self._lazy[i]

    def prod(self, s, e):
        '''[s, e)'''
        self._propagates(*self._gindex(s, e))
        res = self._e()
        s += self._size
        e += self._size
        while s < e:
            if s & 1:
                res = self._op(res, self._d[s])
                s += 1
            if e & 1:
                res = self._op(res, self._d[e - 1])
            s >>= 1
            e >>= 1
        return res


class LazySegTreeRUQ:
    '''区間更新用'''

    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        self._lazy = [None] * (self._size << 1)
        if v is not None:
            for i in range(n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def _gindex(self, s, e):
        s += self._size
        e += self._size
        lm = s >> (s & -s).bit_length()
        rm = e >> (e & -e).bit_length()
        while e > s:
            if s <= lm:
                yield s
            if e <= rm:
                yield e
            e >>= 1
            s >>= 1
        while s:
            yield s
            s >>= 1

    def _propagates(self, *ids):
        for i in reversed(ids):
            v = self._lazy[i]
            if v is None:
                continue
            self._lazy[i] = None
            self._lazy[i << 1] = v
            self._lazy[i << 1 | 1] = v
            self._d[i << 1] = v
            self._d[i << 1 | 1] = v

    def update(self, s, e, x):
        '''[s, e)'''
        ids = self._gindex(s, e)
        self._propagates(*self._gindex(s, e))
        s += self._size
        e += self._size
        while s < e:
            if s & 1:
                self._lazy[s] = x
                self._d[s] = x
                s += 1
            if e & 1:
                self._lazy[e - 1] = x
                self._d[e - 1] = x
            e >>= 1
            s >>= 1
        for i in ids:
            self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def prod(self, s, e):
        '''[s, e)'''
        self._propagates(*self._gindex(s, e))
        res = self._e()
        s += self._size
        e += self._size
        while s < e:
            if s & 1:
                res = self._op(res, self._d[s])
                s += 1
            if e & 1:
                res = self._op(res, self._d[e - 1])
            s >>= 1
            e >>= 1
        return res


def example():
    def op(x, y): return max(x, y)
    def e(): return 0
    st = LazySegTreeRAQ(op, e, 100)
    st.add(0, 10, 1)
    st.add(5, 15, 2)
    print(st.prod(0, 100))
    print(st.prod(0, 5))
    print(st.prod(0, 10))
    print(st.prod(5, 10))
    print(st.prod(10, 15))
    print(st.prod(15, 100))

    def op(x, y): return max(x, y)
    def e(): return 0
    st = LazySegTreeRUQ(op, e, 100)
    st.update(0, 10, 1)
    print(st.prod(0, 5))
    print(st.prod(0, 10))
    print(st.prod(10, 15))
    st.update(5, 15, 2)
    print(st.prod(0, 5))
    print(st.prod(0, 10))
    print(st.prod(10, 15))


if __name__ == '__main__':
    example()
