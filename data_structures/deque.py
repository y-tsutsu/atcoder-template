class Deque:
    def __init__(self, capacity=1024):
        self._size = capacity * 2 - 1
        self._a = [None for _ in range(self._size)]
        self._s = capacity - 1
        self._e = self._s

    def _resize(self):
        nsize = self._size * 2
        na = [None for _ in range(nsize)]
        w = self._e - self._s
        mid = (nsize - w) // 2
        na[mid:mid + w] = self._a[self._s:self._e]
        self._a = na
        self._s = mid
        self._e = mid + w
        self._size = nsize

    def append(self, x):
        if self._e >= self._size:
            self._resize()
        self._a[self._e] = x
        self._e += 1

    def appendleft(self, x):
        if self._s == 0:
            self._resize()
        self._s -= 1
        self._a[self._s] = x

    def pop(self):
        assert self._s != self._e
        self._e -= 1
        return self._a[self._e]

    def popleft(self):
        assert self._s != self._e
        x = self._a[self._s]
        self._s += 1
        return x

    def __str__(self):
        return f'{self._a[self._s: self._e]}'

    def __len__(self):
        return self._e - self._s

    def __getitem__(self, i):
        w = self._e - self._s
        if i < 0:
            i += w
        assert 0 <= i < w
        return self._a[self._s + i]

    def __setitem__(self, i, x):
        w = self._e - self._s
        if i < 0:
            i += w
        assert 0 <= i < w
        self._a[self._s + i] = x

    def __contains__(self, x):
        return x in self._a[self._s:self._e]

    def __iter__(self):
        for i in range(self._s, self._e):
            yield self._a[i]
