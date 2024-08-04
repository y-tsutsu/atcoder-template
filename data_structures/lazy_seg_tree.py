# https://github.com/shakayami/ACL-for-python/wiki/lazysegtree
# https://betrue12.hateblo.jp/entry/2020/09/22/194541

class LazySegTree():
    def __init__(self, op, e, n, mapping, composition, identity, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << (n - 1).bit_length()
        self._d = [self._e()] * (self._size << 1)
        self._lazy = [identity] * (self._size << 1)
        self._mapping = mapping
        self._composition = composition
        self._id = identity
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)

    def _update(self, i):
        self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def _all_apply(self, i, f):
        self._d[i] = self._mapping(f, self._d[i])
        if i < self._size:
            self._lazy[i] = self._composition(f, self._lazy[i])

    def _push(self, i):
        self._all_apply(i << 1, self._lazy[i])
        self._all_apply(i << 1 | 1, self._lazy[i])
        self._lazy[i] = self._id

    def set(self, p, x):
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p):
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, s, e):
        if s == e:
            return self._e()
        s += self._size
        e += self._size
        for i in range(self._log, 0, -1):
            if ((s >> i) << i) != s:
                self._push(s >> i)
            if ((e >> i) << i) != e:
                self._push(e >> i)
        sml, smr = self._e(), self._e()
        while s < e:
            if s & 1:
                sml = self._op(sml, self._d[s])
                s += 1
            if e & 1:
                e -= 1
                smr = self._op(self._d[e], smr)
            s >>= 1
            e >>= 1
        return self._op(sml, smr)

    def all_prod(self):
        return self._d[1]

    def apply_point(self, p, f):
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = self._mapping(f, self._d[p])
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def apply(self, s, e, f):
        if s == e:
            return
        s += self._size
        e += self._size
        for i in range(self._log, 0, -1):
            if ((s >> i) << i) != s:
                self._push(s >> i)
            if ((e >> i) << i) != e:
                self._push((e - 1) >> i)
        l2, r2 = s, e
        while s < e:
            if s & 1:
                self._all_apply(s, f)
                s += 1
            if e & 1:
                e -= 1
                self._all_apply(e, f)
            s >>= 1
            e >>= 1
        s, e = l2, r2
        for i in range(1, self._log+1):
            if ((s >> i) << i) != s:
                self._update(s >> i)
            if ((e >> i) << i) != e:
                self._update((e - 1) >> i)

    def max_right(self, s, g):
        if s == self._n:
            return self._n
        s += self._size
        for i in range(self._log, 0, -1):
            self._push(s >> i)
        sm = self._e
        while True:
            while s % 2 == 0:
                s >>= 1
            if not g(self._op(sm, self._d[s])):
                while s < self._size:
                    self._push(s)
                    s = (2 * s)
                    if g(self._op(sm, self._d[s])):
                        sm = self._op(sm, self._d[s])
                        s += 1
                return s-self._size
            sm = self._op(sm, self._d[s])
            s += 1
            if (s & -s) == s:
                break
        return self._n

    def min_left(self, r, g):
        if r == 0:
            return 0
        r += self._size
        for i in range(self._log, 0, -1):
            self._push((r-1) >> i)
        sm = self._e
        while True:
            r -= 1
            while r > 1 and (r % 2):
                r >>= 1
            if not g(self._op(self._d[r], sm)):
                while r < self._size:
                    self._push(r)
                    r = (2*r+1)
                    if g(self._op(self._d[r], sm)):
                        sm = self._op(self._d[r], sm)
                        r -= 1
                return r+1-self._size
            sm = self._op(self._d[r], sm)
            if (r & -r) == r:
                break
        return 0


def example():
    '''区間和を取るサンプル'''
    def op(x, y):
        vx, lx = x
        vy, ly = y
        return vx + vy, lx + ly

    def e():
        return (0, 0)

    def mapping(f, x):
        vx, lx = x
        return vx + lx * f, lx

    def composition(f, g):
        return f + g

    _id = 0

    st = LazySegTree(op, e, 100, mapping, composition, _id,
                     v=[(0, 1) for _ in range(100)])  # 初期値は長さを1にしたものが必須．e()の値ではダメ．
    print(st.prod(0, 100)[0])
    st.apply(0, 10, 1)
    st.apply(5, 15, 2)
    print(st.prod(0, 5)[0])
    print(st.prod(5, 10)[0])
    print(st.prod(10, 15)[0])
    print(st.prod(0, 15)[0])
    print(st.prod(0, 100)[0])


if __name__ == '__main__':
    example()
