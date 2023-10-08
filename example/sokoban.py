# https://atcoder.jp/contests/abc323/tasks/abc323_f

def sokoban(xa, ya, xb, yb, xc, yc):
    def dist(x1, y1, x2, y2): return abs(x1 - x2) + abs(y1 - y2)

    # | -
    tot1 = 0
    if yb < yc:
        xs, ys = xb, yb - 1
        if xa == xb and ya > yb:
            tot1 += 2
    else:
        xs, ys = xb, yb + 1
        if xa == xb and ya < yb:
            tot1 += 2
    tot1 += dist(xa, ya, xs, ys)
    tot1 += dist(xb, yb, xc, yc)
    if xb != xc:
        tot1 += 2

    # - |
    tot2 = 0
    if xb < xc:
        xs, ys = xb - 1, yb
        if ya == yb and xa > xb:
            tot2 += 2
    else:
        xs, ys = xb + 1, yb
        if ya == yb and xa < xb:
            tot2 += 2
    tot2 += dist(xa, ya, xs, ys)
    tot2 += dist(xb, yb, xc, yc)
    if yb != yc:
        tot2 += 2

    return min(tot1, tot2)
