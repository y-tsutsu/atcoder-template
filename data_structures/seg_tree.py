class SegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1

    def get(self, p):
        return self._d[p + self._size]

    def prod(self, s, e):
        '''[s, e)'''
        sml, smr = self._e(), self._e()
        s += self._size
        e += self._size
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

    def update(self, p, x, func):
        y = self.get(p)
        self.set(p, func(x, y))


class SegTreeAddRange:
    '''区間加算用Segtree'''

    def __init__(self, n, v=None):
        def op(x, y): return x + y
        def e(): return 0
        self._st = SegTree(op, e, n, v)

    def add(self, s, e, x):
        '''[s, e)'''
        self._st.update(s, x, lambda x, y: x + y)
        self._st.update(e, -x, lambda x, y: x + y)

    def get(self, p):
        return self._st.prod(0, p + 1)


def example():
    # 二項演算（二つの値からどう計算するか．指定区間の最大値を求めたい場合はmaxをとるなど．）
    def op(x, y): return max(x, y)
    # 単位元（加算する場合は0，掛け合わせる場合は1など）
    def e(): return 0
    st = SegTree(op, e, 100)
    st.set(10, 42)
    st.set(90, 23)
    print(st.prod(0, 50))
    print(st.prod(90, 100))
    print(st.prod(5, 95))
    print(st.prod(11, 90))


if __name__ == '__main__':
    example()
