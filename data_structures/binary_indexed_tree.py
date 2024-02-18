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


class BITAddRange:
    '''区間加算用BIT'''

    def __init__(self, n):
        self._bit = BIT(n)

    def add(self, s, e, x):
        '''[s, e)'''
        self._bit.add(s, x)
        self._bit.add(e, -x)

    def get(self, p):
        return self._bit.sum(0, p + 1)


class BITHelper:
    def __init__(self, n):
        self._bit = BIT(n)

    def set(self, p, x):
        y = self.get(p)
        self._bit.add(p, x - y)

    def get(self, p):
        return self._bit.sum(p, p + 1)
