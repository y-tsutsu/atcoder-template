class StrHash:
    def __init__(self, s, mod=10 ** 9 + 7):
        self.str = s
        self.mod = mod
        self.h = self._init_hash()

    def get_hash(self, s, e):
        v = self.h[e + 1] - (self.h[s] * self._mpow(100, e - s + 1, self.mod) % self.mod)
        v %= self.mod
        return v

    def _init_hash(self):
        h = [0]
        for i, c in enumerate(self.str):
            x = (100 * h[i] + self._ctoi(c)) % self.mod
            h.append(x)
        return h

    def _ctoi(self, c):
        return ord(c) - ord('a') + 1

    def _mpow(self, base, exp, mod):
        if exp == 0:
            return 1
        a = [i for i, x in enumerate(f'{exp:b}'[::-1]) if x == '1']
        i, j, p, ret = 1, 0, base, 1
        if a[0] == 0:
            j += 1
            ret *= base
            ret %= mod
        while j < len(a):
            p = (p ** 2) % mod
            if i == a[j]:
                ret *= p
                ret %= mod
                j += 1
            i += 1
        return ret
