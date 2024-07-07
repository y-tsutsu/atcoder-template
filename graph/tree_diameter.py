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
