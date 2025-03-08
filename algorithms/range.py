class Range():
    def __init__(self, s, e):
        assert s <= e
        self.s, self.e = s, e

    def __iter__(self): return (i for i in range(self.s, self.e))

    def __reversed__(self): return (i for i in reversed(range(self.s, self.e)))

    def __eq__(self, other): return self.s == other.s and self.e == other.e

    def __len__(self): return self.e - self.s

    def __str__(self): return f'({self.s}, {self.e})'

    def __contains__(self, x): return self.s <= x < self.e if isinstance(x, int) else self.s <= x.s and x.e <= self.e if isinstance(x, Range) else False

    def is_overlaps(self, other): return max(self.s, other.s) < min(self.e, other.e)

    def overlaps(self, other):
        if not self.is_overlaps(other):
            return Range(0, 0)
        return Range(max(self.s, other.s), min(self.e, other.e))

    def diff(self, other):
        if self.is_overlaps(other):
            return -1
        return abs(max(self.s, other.s) - min(self.e, other.e))
