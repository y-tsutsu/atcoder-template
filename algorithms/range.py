class Range():
    def __init__(self, s, e):
        assert s <= e
        self.s, self.e = s, e

    def __iter__(self): return (i for i in range(self.s, self.e))

    def __reversed__(self): return (i for i in reversed(range(self.s, self.e)))

    def __eq__(self, other): return self.s == other.s and self.e == other.e

    def __len__(self): return self.e - self.s

    def __str__(self): return f'({self.s}, {self.e})'

    def __contains__(self, x): return self.s <= x < self.e

    def is_overlaps(self, other): return max(self.s, other.s) < min(self.e, other.e)

    def overlaps(self, other):
        if not self.is_overlaps(other):
            return Range(0, 0)
        return Range(max(self.s, other.s), min(self.e, other.e))

    def diff(self, other):
        if self.is_overlaps(other):
            return -1
        return abs(max(self.s, other.s) - min(self.e, other.e))


def example():
    r05 = Range(0, 5)
    r04 = Range(0, 4)
    for i in r05:
        print(i)
    for j in reversed(r05):
        print(j)
    print(r05 == Range(0, 5))
    print(r05 == r04)
    print(len(r05), len(r04))
    print(len(Range(-5, 5)))
    print(r05)
    print(0 in r05)
    print(5 in r05)
    print(Range(0, 5).is_overlaps(Range(4, 10)), Range(0, 5).overlaps(Range(4, 10)))
    print(Range(0, 5).is_overlaps(Range(5, 10)), Range(0, 5).overlaps(Range(5, 10)))
    print(Range(5, 10).is_overlaps(Range(0, 6)), Range(5, 10).overlaps(Range(0, 6)))
    print(Range(5, 10).is_overlaps(Range(0, 5)), Range(5, 10).overlaps(Range(0, 5)))
    print(Range(0, 5).diff(Range(4, 10)))
    print(Range(0, 5).diff(Range(5, 10)))
    print(Range(0, 5).diff(Range(6, 10)))
    print(Range(5, 10).diff(Range(0, 6)))
    print(Range(5, 10).diff(Range(0, 5)))
    print(Range(5, 10).diff(Range(0, 4)))


if __name__ == '__main__':
    example()
