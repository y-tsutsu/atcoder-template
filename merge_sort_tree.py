from bisect import bisect_left, bisect_right
from heapq import merge


class MergeSortTree:
    def __init__(self, n, a):
        self._n = 1 << (n - 1).bit_length()
        self._d = [None for _ in range(2 * self._n)]
        for i, x in enumerate(a):
            self._d[self._n - 1 + i] = [x]
        for i in range(n, self._n):
            self._d[self._n - 1 + i] = []
        for i in range(self._n - 2, -1, -1):
            *self._d[i], = merge(self._d[2 * i + 1], self._d[2 * i + 2])

    def query(self, s, e, x):
        '''count elements self._d[i] <= x in [s, e)'''
        l, r = s + self._n, e + self._n
        ret = 0
        while l < r:
            if r & 1:
                r -= 1
                ret += bisect_right(self._d[r - 1], x)
            if l & 1:
                ret += bisect_right(self._d[l - 1], x)
                l += 1
            l >>= 1
            r >>= 1
        return ret

    def queryex(self, s, e, x, y):
        '''count elements x <= self._d[i] <= y in [s, e)'''
        l, r = s + self._n, e + self._n
        ret = 0
        while l < r:
            if r & 1:
                r -= 1
                ret += bisect_right(self._d[r - 1], y) - bisect_left(self._d[r - 1], x)
            if l & 1:
                ret += bisect_right(self._d[l - 1], y) - bisect_left(self._d[l - 1], x)
                l += 1
            l >>= 1
            r >>= 1
        return ret
