from random import randint


class RollingHash:
    def __init__(self, s, mod=998244353, base=randint(100, 500)):
        self._str = s
        self._mod = mod
        self._base = base
        self._h = self._init_hash()

    def get_hash(self, s, e):
        '''[s, e)'''
        v = self._h[e] - (self._h[s] * pow(self._base, e - s, self._mod) % self._mod)
        v %= self._mod
        return v

    def _init_hash(self):
        h = [0]
        for i, c in enumerate(self._str):
            x = (self._base * h[i] + self._ctoi(c)) % self._mod
            h.append(x)
        return h

    def _ctoi(self, c):
        return ord(c) - ord('a') + 1


class SegTree:
    pass


class SegRollingHash:
    def __init__(self, s, mod=998244353, base=randint(100, 500)):
        self._mod = mod
        self._n = len(s)
        self._pow = [1]
        for _ in range(self._n):
            self._pow.append(self._pow[-1] * base % self._mod)
        self._st = self._init_hash(self._n)
        for i, c in enumerate(s):
            self.set(i, c)
        self._pow = [1]
        for _ in range(self._n):
            self._pow.append(self._pow[-1] * base % self._mod)

    def _init_hash(self, n):
        def op(x, y):
            (vx0, vx1, sx, ex), (vy0, vy1, sy, ey) = x, y
            if sx == ex:
                return y
            if sy == ey:
                return x
            if sx > sy:
                vx0, vx1, sx, ex, vy0, vy1, sy, ey = vy0, vy1, sy, ey, vx0, vx1, sx, ex
            if ex == sy:
                return [(vx0 * self._pow[ey - sy] + vy0) % self._mod,
                        (vy1 * self._pow[ex - sx] + vx1) % self._mod,
                        sx, ey]
            if sx <= sy and ey <= ex:
                return x
            elif sy <= sx and ex <= ey:
                return y
            else:
                assert False

        def e(): return (0, 0, 0, 0)

        return SegTree(op, e, n)

    def get_hash(self, s, e):
        '''（a ハッシュ， b 反転文字のハッシュ）: [s, e)'''
        a, b, _, _ = self._st.prod(s, e)
        return a, b

    def set(self, p, c):
        v = ord(c) - ord('a') + 1
        self._st.set(p, (v, v, p, p + 1))
