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
