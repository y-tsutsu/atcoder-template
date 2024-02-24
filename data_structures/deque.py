class Deque:
    def __init__(self, capacity=10**7):
        self._size = capacity * 2 - 1
        self._a = [None for _ in range(self._size)]
        self._s = capacity - 1
        self._e = self._s

    def append(self, x):
        if self._s == self._e:
            self._e += 1
            self._a[self._s] = x
        else:
            if self._e >= self._size:
                raise BufferError
            self._e += 1
            self._a[self._e - 1] = x

    def appendleft(self, x):
        if self._s == self._e:
            self._e += 1
            self._a[self._s] = x
        else:
            if self._s - 1 < 0:
                raise BufferError
            self._s -= 1
            self._a[self._s] = x

    def pop(self):
        if self._s == self._e:
            raise BufferError
        self._e -= 1
        return self._a[self._e]

    def popleft(self):
        if self._s == self._e:
            raise BufferError
        self._s += 1
        return self._a[self._s + 1]

    def __str__(self):
        return f'{self._a[self._s: self._e]}'

    def __len__(self):
        return self._e - self._s

    def __getitem__(self, i):
        w = self._e - self._s
        if i < 0:
            i = w + i
        if i < 0 or i >= w:
            raise BufferError
        return self._a[self._s + i]

    def __contains__(self, x):
        return x in self._a[self._s: self._e]

    def __iter__(self):
        for i in range(self._e - self._s):
            yield self._a[self._s + i]
