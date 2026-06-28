class DualSegTree:
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        self._v = [self._e()] * self._n if v is None else list(v)

    def apply(self, s, e, x):
        s += self._size
        e += self._size
        while s < e:
            if s & 1:
                self._d[s] = self._op(self._d[s], x)
                s += 1
            if e & 1:
                e -= 1
                self._d[e] = self._op(self._d[e], x)
            s >>= 1
            e >>= 1

    def get(self, p):
        ret = self._v[p]
        p += self._size
        while p:
            ret = self._op(ret, self._d[p])
            p >>= 1
        return ret

    def set(self, p, x):
        self._v[p] = x


def example():
    def op(x, y): return max(x, y)
    def e(): return 0
    st = DualSegTree(op, e, 100)
    st.apply(10, 30, 42)
    st.apply(20, 40, 23)
    st.set(99, 100)
    print(0, st.get(0))
    print(10, st.get(10))
    print(20, st.get(20))
    print(30, st.get(30))
    print(40, st.get(40))
    print(99, st.get(99))


if __name__ == '__main__':
    example()
