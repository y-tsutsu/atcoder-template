from functools import lru_cache
from math import factorial


def perm(n, r):
    ret = 1
    for i in range(r):
        ret *= n - i
    return ret


def comb(n, r):
    return perm(n, r) // perm(r, r)


def combr(n, r):
    return comb(n + r - 1, r)


def factorial_perm(n, r):
    return factorial(n) // factorial(n - r)


def factorial_comb(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


@lru_cache(maxsize=1000000)
def pascal_comb(n, r):
    if r == 0 or n == r:
        return 1
    return pascal_comb(n - 1, r - 1) + pascal_comb(n - 1, r)
