# https://atcoder.jp/contests/abc331/tasks/abc331_d

def accumulate2dim(a):
    pass


def acm2dim_helper(a):
    pass


def tile(a, b, c, d, h, w, p):
    def inner(i, j, h, w, acm):
        hc, wc = (i + 1) // h, (j + 1) // w
        hm, wm = (i + 1) % h, (j + 1) % w
        ret = hc * wc * acm(0, 0, h, w)
        ret += hc * acm(0, 0, h, wm)
        ret += wc * acm(0, 0, hm, w)
        ret += acm(0, 0, hm, wm)
        return ret
    acm = acm2dim_helper(p)
    return inner(c, d, h, w, acm) - inner(a - 1, d, h, w, acm) - inner(c, b - 1, h, w, acm) + inner(a - 1, b - 1, h, w, acm)
