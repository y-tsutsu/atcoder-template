class Manacher:
    def __init__(self, s):
        self._n = len(s)
        self._m = 2 * self._n + 1
        self._r = self._initialize(s)

    def _initialize(self, s):
        ret = [0 for _ in range(self._m)]
        i, j = 0, 0
        while i < self._m:
            while j <= i < self._m - j and self._compare(s, i - j, i + j):
                j += 1
            ret[i] = j
            k = 1
            while k <= i < self._m - k and k + ret[i - k] < j:
                ret[i + k] = ret[i - k]
                k += 1
            i += k
            j -= k
        return ret

    def _compare(self, s, le, ri):
        return s[le // 2] == s[ri // 2] if le & 1 else True

    def judge(self, s, e):
        '''[s, e)'''
        m = s + e
        return 2 * e - 1 < m + self._r[m]

    def max_length(self):
        return max(self._r) - 1


def example():
    a = [1, 0, 0, 0, 1, 2]
    m = Manacher(a)
    for i in range(6):
        for j in range(i + 1, 7):
            print(a[i:j], m.judge(i, j))
    print(m.max_length())


if __name__ == '__main__':
    example()
