from sys import maxsize


class SegTree:
    pass


def manhattan_mst(n, xs, ys):
    '''各座標から他座標のうちマンハッタン距離の最小値を算出'''
    assert n == len(xs) == len(ys)
    INF = maxsize
    ret = [INF for _ in range(n)]

    xy = [(x, y, i) for i, (x, y) in enumerate(zip(xs, ys))]
    xy.sort()
    x = [x for x, _, _ in xy]
    y = [y for _, y, _ in xy]
    indices = [i for _, _, i in xy]
    values = sorted(set(y))
    ranks = {v: i for i, v in enumerate(values)}
    yi = [ranks[v] for v in y]
    m = len(values)

    def op(x, y): return min(x, y)
    def e(): return INF

    # xi > xj, yi > yj
    st = SegTree(op, e, m)
    for i in range(n):
        v = st.prod(0, yi[i] + 1)
        if v != INF:
            ret[indices[i]] = min(ret[indices[i]], x[i] + y[i] + v)
        st.set(yi[i], -x[i] - y[i])

    # xi > xj, yi < yj
    st = SegTree(op, e, m)
    for i in range(n):
        v = st.prod(yi[i], m)
        if v != INF:
            ret[indices[i]] = min(ret[indices[i]], x[i] - y[i] + v)
        st.set(yi[i], -x[i] + y[i])

    # xi < xj, yi > yj
    st = SegTree(op, e, m)
    for i in range(n - 1, -1, -1):
        v = st.prod(0, yi[i] + 1)
        if v != INF:
            ret[indices[i]] = min(ret[indices[i]], -x[i] + y[i] + v)
        st.set(yi[i], x[i] - y[i])

    # xi < xj, yi < yj
    st = SegTree(op, e, m)
    for i in range(n - 1, -1, -1):
        v = st.prod(yi[i], m)
        if v != INF:
            ret[indices[i]] = min(ret[indices[i]], -x[i] - y[i] + v)
        st.set(yi[i], x[i] + y[i])

    return ret


def rotate_45_deg(xys):
    return [(x + y, x - y) for x, y in xys]


def manhattan_max(xys):
    '''全座標の組合せの中でマンハッタン距離の最大値を算出'''
    # https://fukubutyo.web.fc2.com/Manhattan.html
    p = rotate_45_deg(xys)  # 45度回転のルート2倍の座標
    xs = [x for x, _ in p]
    ys = [y for _, y in p]
    ret = max(max(xs) - min(xs), max(ys) - min(ys))
    return ret
