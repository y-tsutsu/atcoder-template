class FlatList2D:
    def __init__(self, h, w, initial=0):
        self.h = h
        self.w = w
        self.p = [initial for _ in range(h * w)]

    def __getitem__(self, idx):
        i, j = idx
        return self.p[i * self.w + j]

    def __setitem__(self, idx, value):
        i, j = idx
        self.p[i * self.w + j] = value

    def __iter__(self): return (i for i in self.p)

    def __eq__(self, other): return self.h == other.h and self.w == other.w and self.p == other.p

    def __len__(self): return len(self.p)

    def __str__(self): return '\n'.join(str(row) for row in [self.p[i * self.w:(i + 1) * self.w] for i in range(self.h)])

    def __contains__(self, x): return x in self.p

    def copy(self):
        new = FlatList2D(self.h, self.w)
        new.p = self.p[:]
        return new


def example():
    p = FlatList2D(3, 5)
    p[2, 3] = 42
    print(p[2, 3])
    print(p)


if __name__ == '__main__':
    example()
