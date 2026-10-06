from functools import total_ordering


@total_ordering
class Range():
    def __init__(self, s, e):
        assert s <= e
        self.s, self.e = s, e

    def __iter__(self): return (i for i in range(self.s, self.e))

    def __reversed__(self): return (i for i in reversed(range(self.s, self.e)))

    def __eq__(self, other): return self.s == other.s and self.e == other.e

    def __lt__(self, other): return (self.s, self.e) < (other.s, other.e)

    def __len__(self): return self.e - self.s

    def __str__(self): return f'[{self.s}, {self.e})'

    def __contains__(self, x): return self.s <= x < self.e if isinstance(x, int) else self.s <= x.s and x.e <= self.e if isinstance(x, Range) else False

    def overlaps(self, other): return max(self.s, other.s) < min(self.e, other.e)

    def and_range(self, other): return Range(max(self.s, other.s), min(self.e, other.e)) if self.overlaps(other) else None

    def or_range(self, other): return Range(min(self.s, other.s), max(self.e, other.e)) if self.gap(other) <= 0 else None

    def gap(self, other): return abs(max(self.s, other.s) - min(self.e, other.e)) if not self.overlaps(other) else -1


def merge_ranges(ranges):
    ranges = sorted(r for r in ranges if len(r) > 0)
    if not ranges:
        return []

    ret = [ranges[0]]
    for r in ranges[1:]:
        merged = ret[-1].or_range(r)
        if merged is None:
            ret.append(r)
        else:
            ret[-1] = merged
    return ret


def example():
    a = Range(1, 5)  # [1, 5): 1以上5未満
    b = Range(3, 7)  # [3, 7): 3以上7未満
    print(a.overlaps(b))       # True: 共通部分がある
    print(a.and_range(b))      # [3, 5): AND（共通部分）
    print(a.or_range(b))       # [1, 7): OR（両方を含む区間）
    print(a.gap(b))            # -1: 重なっている

    c = Range(5, 8)            # aの右端とcの左端が接する
    print(a.overlaps(c))       # False: 半開区間なので重ならない
    print(a.and_range(c))      # None: 共通部分なし
    print(a.or_range(c))       # [1, 8): 接している区間は結合できる
    print(a.gap(c))            # 0: 区間同士が接している

    d = Range(7, 9)
    print(a.or_range(d))       # None: 離れた区間は一つに結合できない
    print(a.gap(d))            # 2: 区間同士の距離

    ranges = [Range(7, 9), Range(1, 3), Range(2, 5), Range(5, 7), Range(11, 12)]
    print(*merge_ranges(ranges))  # [1, 9) [11, 12)


if __name__ == '__main__':
    example()
