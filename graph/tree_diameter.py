from collections import deque


def diameter(n, to):
    def bfs(i, d):
        dq = deque()
        dq.append(i)
        while dq:
            i = dq.popleft()
            for j, c in to[i]:  # toは重み付き隣接リスト
                if d[j] != -1:
                    continue
                d[j] = d[i] + c
                dq.append(j)

    d = [-1 for _ in range(n)]
    d[0] = 0
    bfs(0, d)
    m = max(d)
    s = [i for i, x in enumerate(d) if x == m][0]
    d = [-1 for _ in range(n)]
    d[s] = 0
    bfs(s, d)
    m = max(d)
    e = [i for i, x in enumerate(d) if x == m][0]
    return s, e, m


def recurboost(func=None, stack=[]):
    pass


def route(s, e, to):
    @recurboost
    def dfs(i, p, route):
        route.append(i)
        if i == e:
            yield True
        for j, _ in to[i]:  # toは重み付き隣接リスト
            if j == p:
                continue
            r = yield dfs(j, i, route)
            if r:
                yield True
        route.pop()
        yield False

    ret = []
    dfs(s, -1, ret)
    return ret


def rerooting_dp(n, to):
    '''全方位木DPでの木の直径算出'''
    d = [0 for _ in range(n)]

    @recurboost
    def dfs(i, p):
        ret = 0
        for j in to[i]:
            if j == p:
                continue
            r = yield dfs(j, i)
            ret = max(ret, r + 1)
        d[i] = ret
        yield ret

    dfs(0, -1)

    @recurboost
    def dfs2(i, p, pv):
        a = [(0, -1)]  # 番兵
        for j in to[i]:
            if j == p:
                a.append((pv + 1, j))
            else:
                a.append((d[j] + 1, j))
        a.sort(reverse=True)
        ret = sum([u for u, _ in a[:2]])
        for j in to[i]:
            if j == p:
                continue
            npv = a[0][0] if a[0][1] != j else a[1][0]
            r = yield dfs2(j, i, npv)
            ret = max(ret, r)
        yield ret

    ret = dfs2(0, -1, 0)
    return ret
