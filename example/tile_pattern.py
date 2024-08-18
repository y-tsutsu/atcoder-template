# https://atcoder.jp/contests/abc331/tasks/abc331_d

def accumulate2dim(a):
    pass


def acm2dim_helper(a):
    pass


def tile(si, sj, ei, ej, h, w, p):
    acm = acm2dim_helper(p)

    def inner(i, j):
        ch, cw = i // h, j // w
        mh, mw = i % h, j % w
        ret = acm(0, 0, h, w) * (ch * cw)
        ret += acm(0, 0, h, mw) * ch
        ret += acm(0, 0, mh, w) * cw
        ret += acm(0, 0, mh, mw)
        return ret

    return inner(ei, ej) - inner(si, ej) - inner(ei, sj) + inner(si, sj)
