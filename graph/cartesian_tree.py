from collections import deque


class SegTree:
    pass


def cartesian_tree(n, p):
    def op(x, y): return max(x, y)
    def e(): return -1
    st = SegTree(op, e, n, p)
    to = [[] for _ in range(n)]
    pos = {x: i for i, x in enumerate(p)}
    dq = deque()
    dq.append((n, (0, n)))
    while dq:
        v, (le, ri) = dq.popleft()
        i = pos[v]
        lev, riv = st.prod(le, i), st.prod(i + 1, ri)
        if lev != e():
            to[i].append(pos[lev])
            dq.append((lev, (le, i)))
        if riv != e():
            to[i].append(pos[riv])
            dq.append((riv, (i + 1, ri)))
    return to
