from itertools import accumulate


def acm_helper(a):
    acm = list(accumulate(a, initial=0))

    def helper(s, e):
        return acm[e] - acm[s]

    return helper


def accumulate2dim(a):
    h, w = len(a), len(a[0])
    p = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    for i in range(h):
        for j in range(w):
            p[i + 1][j + 1] = p[i + 1][j] + a[i][j]
    for j in range(w + 1):
        for i in range(h):
            p[i + 1][j] += p[i][j]
    return p


def acm2dim_helper(a):
    acm = accumulate2dim(a)

    def helper(si, sj, ei, ej):
        return acm[ei][ej] - acm[si][ej] - acm[ei][sj] + acm[si][sj]

    return helper


def imos2d_helper(h, w):
    p = [[0 for _ in range(w + 1)] for _ in range(h + 1)]

    def set_helper(si, sj, ei, ej):
        for i, j, v in [(si, sj, 1), (ei, sj, -1), (si, ej, -1), (ei, ej, 1)]:
            p[i][j] += v

    def acm_helper(): return accumulate2dim(p)

    return set_helper, acm_helper
