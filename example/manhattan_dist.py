from sys import maxsize


class SegTree:
    pass


def manhattan_mst(n, xs, ys):
    '''各座標から他座標のうちマンハッタン距離の最小値を算出'''
    INF = maxsize
    ret = [INF for _ in range(n)]

    xy = [(i, j) for i, j in zip(xs, ys)]
    xy.sort()
    x = [x for x, _ in xy]
    y = [y for _, y in xy]

    def op(x, y): return min(x, y)
    def e(): return INF

    # xi > xj, yi > yj
    st = SegTree(op, e, n)
    for i in range(n):
        v = st.prod(0, y[i] + 1)
        if v != -INF:
            ret[i] = min(ret[i], x[i] + y[i] + v)
        st.set(y[i], -x[i] - y[i])

    # xi > xj, yi < yj
    st = SegTree(op, e, n)
    for i in range(n):
        v = st.prod(y[i], n)
        if v != INF:
            ret[i] = min(ret[i], x[i] - y[i] + v)
        st.set(y[i], -x[i] + y[i])

    # xi < xj, yi > yj
    st = SegTree(op, e, n)
    for i in range(n - 1, -1, -1):
        v = st.prod(0, y[i] + 1)
        if v != INF:
            ret[i] = min(ret[i], -x[i] + y[i] + v)
        st.set(y[i], x[i] - y[i])

    # xi < xj, yi < yj
    st = SegTree(op, e, n)
    for i in range(n - 1, -1, -1):
        v = st.prod(y[i], n)
        if v != INF:
            ret[i] = min(ret[i], -x[i] - y[i] + v)
        st.set(y[i], x[i] + y[i])

    return ret


def manhattan_max(xys):
    '''全座標の組合せの中でマンハッタン距離の最大値を算出'''
    # https://fukubutyo.web.fc2.com/Manhattan.html
    p = [(x + y, x - y) for x, y in xys]  # 45度回転のルート2倍の座標
    xs = [x for x, _ in p]
    ys = [y for _, y in p]
    ret = max(max(xs) - min(xs), max(ys) - min(ys))
    return ret
