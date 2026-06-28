class OfflineDualSegTree:
    def __init__(self, op, e, n):
        self._n = n
        self._op = op
        self._size = 1 << (n - 1).bit_length()
        self._d = [e()] * (self._size << 1)

    def apply(self, s, e, x):
        s += self._size
        e += self._size
        d = self._d
        op = self._op
        while s < e:
            if s & 1:
                d[s] = op(d[s], x)
                s += 1
            if e & 1:
                e -= 1
                d[e] = op(d[e], x)
            s >>= 1
            e >>= 1

    def build(self):
        d = self._d
        op = self._op
        for i in range(1, self._size):
            d[i << 1] = op(d[i << 1], d[i])
            d[i << 1 | 1] = op(d[i << 1 | 1], d[i])
        return d[self._size:self._size + self._n]


class OfflineDualSegTreeMax:
    def __init__(self, n, e=-(1 << 62)):
        self._n = n
        self._size = 1 << (n - 1).bit_length()
        self._d = [e] * (self._size << 1)

    def apply(self, s, e, x):
        s += self._size
        e += self._size
        while s < e:
            if s & 1:
                if self._d[s] < x:
                    self._d[s] = x
                s += 1
            if e & 1:
                e -= 1
                if self._d[e] < x:
                    self._d[e] = x
            s >>= 1
            e >>= 1

    def build(self):
        for i in range(1, self._size):
            x = self._d[i]
            if self._d[i << 1] < x:
                self._d[i << 1] = x
            if self._d[i << 1 | 1] < x:
                self._d[i << 1 | 1] = x
        return self._d[self._size:self._size + self._n]


class OfflineDualSegTreeMin:
    def __init__(self, n, e=1 << 62):
        self._n = n
        self._size = 1 << (n - 1).bit_length()
        self._d = [e] * (self._size << 1)

    def apply(self, s, e, x):
        s += self._size
        e += self._size
        while s < e:
            if s & 1:
                if self._d[s] > x:
                    self._d[s] = x
                s += 1
            if e & 1:
                e -= 1
                if self._d[e] > x:
                    self._d[e] = x
            s >>= 1
            e >>= 1

    def build(self):
        for i in range(1, self._size):
            x = self._d[i]
            if self._d[i << 1] > x:
                self._d[i << 1] = x
            if self._d[i << 1 | 1] > x:
                self._d[i << 1 | 1] = x
        return self._d[self._size:self._size + self._n]


def example():
    def op(x, y): return max(x, y)
    def e(): return 0
    st = OfflineDualSegTree(op, e, 100)
    st.apply(10, 30, 42)
    st.apply(20, 40, 23)
    p = st.build()
    print(0, p[0])
    print(10, p[10])
    print(20, p[20])
    print(30, p[30])
    print(40, p[40])


if __name__ == '__main__':
    example()
