class BIT:
    def __init__(self, n):
        self._n = n
        self._d = [0 for _ in range(n)]

    def add(self, p, x):
        p += 1
        while p <= self._n:
            self._d[p - 1] += x
            p += p & -p

    def sum(self, s, e):
        '''[s, e)'''
        return self._sum(e) - self._sum(s)

    def _sum(self, e):
        '''[0, e)'''
        s = 0
        while e > 0:
            s += self._d[e - 1]
            e -= e & -e
        return s
