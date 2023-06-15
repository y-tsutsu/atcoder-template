from sys import maxsize


class SegTree:
    pass


def manhattan_mst(n, x, y):
    INF = maxsize
    ret = [INF for _ in range(n)]

    xy = [(i, j) for i, j in zip(x, y)]
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
