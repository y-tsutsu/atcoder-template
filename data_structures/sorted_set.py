import math
from bisect import bisect_left, bisect_right


class SortedSet:
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24

    def __init__(self, a=[]):
        a = list(a)
        n = len(a)
        if any(a[i] > a[i + 1] for i in range(n - 1)):
            a.sort()
        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            a, b = [], a
            for x in b:
                if not a or a[-1] != x:
                    a.append(x)
        n = self._size = len(a)
        num_bucket = int(math.ceil(math.sqrt(n / self.BUCKET_RATIO)))
        self._a = [a[n * i // num_bucket: n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self):
        for i in self._a:
            for j in i:
                yield j

    def __reversed__(self):
        for i in reversed(self._a):
            for j in reversed(i):
                yield j

    def __eq__(self, other):
        return list(self) == list(other)

    def __len__(self):
        return self._size

    def __repr__(self):
        return 'SortedSet' + str(self._a)

    def __str__(self):
        s = str(list(self))
        return '{' + s[1: len(s) - 1] + '}'

    def _position(self, x):
        for i, a in enumerate(self._a):
            if x <= a[-1]:
                break
        return (a, i, bisect_left(a, x))

    def __contains__(self, x):
        if self._size == 0:
            return False
        a, _, i = self._position(x)
        return i != len(a) and a[i] == x

    def add(self, x):
        if self._size == 0:
            self._a = [[x]]
            self._size = 1
            return True
        a, b, i = self._position(x)
        if i != len(a) and a[i] == x:
            return False
        a.insert(i, x)
        self._size += 1
        if len(a) > len(self._a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self._a[b:b+1] = [a[:mid], a[mid:]]
        return True

    def _pop(self, a, b, i):
        ans = a.pop(i)
        self._size -= 1
        if not a:
            del self._a[b]
        return ans

    def discard(self, x):
        if self._size == 0:
            return False
        a, b, i = self._position(x)
        if i == len(a) or a[i] != x:
            return False
        self._pop(a, b, i)
        return True

    def lt(self, x):
        for a in reversed(self._a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x):
        for a in reversed(self._a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x):
        for a in self._a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x):
        for a in self._a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, i):
        if i < 0:
            for a in reversed(self._a):
                i += len(a)
                if i >= 0:
                    return a[i]
        else:
            for a in self._a:
                if i < len(a):
                    return a[i]
                i -= len(a)
        raise IndexError

    def pop(self, i=-1):
        if i < 0:
            for b, a in enumerate(reversed(self._a)):
                i += len(a)
                if i >= 0:
                    return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self._a):
                if i < len(a):
                    return self._pop(a, b, i)
                i -= len(a)
        raise IndexError

    def index(self, x):
        ans = 0
        for a in self._a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x):
        ans = 0
        for a in self._a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

    def max(self):
        return self._a[-1][-1]

    def min(self):
        return self._a[0][0]
