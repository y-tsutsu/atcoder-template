from bisect import bisect_left
from functools import cmp_to_key, total_ordering


@total_ordering
class Comparable:
    '''sortの比較は__lt__()が定義されていればOK'''

    def __init__(self):
        pass

    def __lt__(self, other):
        return True

    def __eq__(self, other):
        return True


def compress(a):
    '''独自クラスでの比較は効率が悪いのでintで座標圧縮する関数'''
    uniq = []
    for x in sorted(a):
        if not uniq or x != uniq[-1]:
            uniq.append(x)
    return [bisect_left(uniq, x) for x in a]


def cmp(u, v):
    '''u: a / b, v: c / d'''
    a, b = u
    c, d = v
    if a * d < c * b:
        return -1
    if a * d > c * b:
        return 1
    return 0


def example():
    a = [(1, 2), (1, 3), (2, 3), (3, 4), (3, 5)]
    a.sort(key=cmp_to_key(cmp))
    print(a)


if __name__ == '__main__':
    example()
