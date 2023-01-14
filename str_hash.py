class StrHash:
    def __init__(self, s, mod=10 ** 9 + 7):
        self.str = s
        self.mod = mod
        self.h = self._init_hash()

    def get_hash(self, s, e):
        v = self.h[e + 1] - (self.h[s] * pow(100, e - s + 1, self.mod) % self.mod)
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
