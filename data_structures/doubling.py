class Doubling:
    def __init__(self, a, max_=64):
        n = len(a)
        self._d = [a[:]]
        self._max = max_
        for _ in range(self._max - 1):
            p = [0 for _ in range(n)]
            for i in range(n):
                p[i] = self._d[-1][self._d[-1][i]]
            self._d.append(p)

    def query(self, pos, n):
        '''posからn回移動する'''
        for i in range(self._max - 1, -1, -1):
            if n >> i & 1 == 0:
                continue
            pos = self._d[i][pos]
        return pos


class DoublingWeight:
    def __init__(self, a, weight, max_=64):
        n = len(a)
        self._d = [a[:]]
        self._e = [weight[:]]
        self._max = max_
        for _ in range(self._max - 1):
            p = [0 for _ in range(n)]
            q = [0 for _ in range(n)]
            for i in range(n):
                p[i] = self._d[-1][self._d[-1][i]]
                q[i] = self._e[-1][i] + self._e[-1][self._d[-1][i]]
            self._d.append(p)
            self._e.append(q)

    def query(self, pos, n):
        '''posからn回移動する'''
        tot = 0
        for i in range(self._max - 1, -1, -1):
            if n >> i & 1 == 0:
                continue
            tot += self._e[i][pos]
            pos = self._d[i][pos]
        return pos, tot
