from itertools import accumulate, product


def acm_helper(a):
    acm = list(accumulate(a, initial=0))
    def helper(s, e): return acm[e] - acm[s]
    return helper


def accumulate2dim(a):
    h, w = len(a), len(a[0])
    p = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    for i, j in product(range(h), range(w)):
        p[i + 1][j + 1] = a[i][j]
    for i, j in product(range(h + 1), range(w)):
        p[i][j + 1] += p[i][j]
    for i, j in product(range(h), range(w + 1)):
        p[i + 1][j] += p[i][j]
    return p


def acm2dim_helper(a):
    acm = accumulate2dim(a)
    def helper(si, sj, ei, ej): return acm[ei][ej] - acm[si][ej] - acm[ei][sj] + acm[si][sj]
    return helper


def accumulate3dim(a):
    d, h, w = len(a), len(a[0]), len(a[0][0])
    p = [[[0 for _ in range(w + 1)] for _ in range(h + 1)] for _ in range(d + 1)]
    for i, j, k in product(range(d), range(h), range(w)):
        p[i + 1][j + 1][k + 1] = a[i][j][k]
    for i, j, k in product(range(d + 1), range(h + 1), range(w)):
        p[i][j][k + 1] += p[i][j][k]
    for i, j, k in product(range(d + 1), range(h), range(w + 1)):
        p[i][j + 1][k] += p[i][j][k]
    for i, j, k in product(range(d), range(h + 1), range(w + 1)):
        p[i + 1][j][k] += p[i][j][k]
    return p


def acm3dim_helper(a):
    acm = accumulate3dim(a)
    def helper(si, sj, sk, ei, ej, ek): return ((acm[ei][ej][ek] - acm[ei][sj][ek] - acm[ei][ej][sk] + acm[ei][sj][sk]) -
                                                (acm[si][ej][ek] - acm[si][sj][ek] - acm[si][ej][sk] + acm[si][sj][sk]))
    return helper


def imos_helper(n):
    p = [0 for _ in range(n + 1)]

    def set_helper(s, e, x):
        p[s] += x
        p[e] -= x

    def acm_helper(): return list(accumulate(p))[:-1]

    return set_helper, acm_helper


def imos2d_helper(h, w):
    p = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    def set_helper(si, sj, ei, ej, x):
        for i, j, v in [(si, sj, x), (ei, sj, -x), (si, ej, -x), (ei, ej, x)]:
            p[i][j] += v

    def acm_helper(): return accumulate2dim(p)

    return set_helper, acm_helper


def imos3d_helper(d, h, w):
    p = [[[0 for _ in range(w + 1)] for _ in range(h + 1)] for _ in range(d + 1)]

    def set_helper(si, sj, sk, ei, ej, ek, x):
        for i, j, k, v in [(si, sj, sk, x), (ei, sj, sk, -x), (si, ej, sk, -x), (ei, ej, sk, x),
                           (si, sj, ek, -x), (ei, sj, ek, x), (si, ej, ek, x), (ei, ej, ek, -x)]:
            p[i][j][k] += v

    def acm_helper(): return accumulate3dim(p)

    return set_helper, acm_helper
