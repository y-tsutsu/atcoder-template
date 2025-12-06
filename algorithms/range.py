from functools import total_ordering


@total_ordering
class Range():
    def __init__(self, s, e): self.s, self.e = s, e

    def __iter__(self): return (i for i in range(self.s, self.e))

    def __reversed__(self): return (i for i in reversed(range(self.s, self.e)))

    def __eq__(self, other): return self.s == other.s and self.e == other.e

    def __lt__(self, other): return (self.s, self.e) < (other.s, other.e)

    def __len__(self): return self.e - self.s

    def __str__(self): return f'({self.s}, {self.e})'

    def __contains__(self, x): return self.s <= x < self.e if isinstance(x, int) else self.s <= x.s and x.e <= self.e if isinstance(x, Range) else False

    def overlaps(self, other): return max(self.s, other.s) < min(self.e, other.e)

    def intersection(self, other): return Range(max(self.s, other.s), min(self.e, other.e)) if self.overlaps(other) else None

    def union(self, other): return Range(min(self.s, other.s), max(self.e, other.e)) if self.overlaps(other) else None

    def gap(self, other): return abs(max(self.s, other.s) - min(self.e, other.e)) if not self.overlaps(other) else -1
