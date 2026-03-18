from functools import cmp_to_key
from math import isqrt


def mo(xy, q, n):
    w = n // isqrt(q)
    e = [x // w for x, y in xy]
    p = [(i, (x, y)) for i, (x, y) in enumerate(xy)]

    def cmp(u, v):
        i, (a, b) = u
        j, (c, d) = v
        if e[i] < e[j]:
            return -1
        if e[i] > e[j]:
            return 1
        if e[i] % 2 == 0:
            if b < d:
                return -1
            if b > d:
                return 1
        else:
            if b < d:
                return 1
            if b > d:
                return -1
        return 0

    p.sort(key=cmp_to_key(cmp))
    return p
