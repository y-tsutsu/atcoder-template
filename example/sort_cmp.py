from functools import cmp_to_key


class Comparable:
    '''sortの比較は__lt__()が定義されていればOK'''

    def __init__(self):
        pass

    def __lt__(self, other):
        pass


def cmp(u, v):
    '''u: a / b, v: c / d'''
    a, b = u
    c, d = v
    if a * d < c * b:
        return -1
    if a * d > c * b:
        return 1
    else:
        return 0


def example():
    a = [(1, 2), (1, 3), (2, 3), (3, 4), (3, 5)]
    a.sort(key=cmp_to_key(cmp))
    print(a)


if __name__ == '__main__':
    example()
