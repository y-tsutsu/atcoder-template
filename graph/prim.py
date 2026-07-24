def prim(cost):
    '''隣接行列から最小全域木を隣接リストで返す'''
    n = len(cost)
    INF = 1 << 62
    used = [0 for _ in range(n)]
    min_cost = [INF for _ in range(n)]
    parent = [-1 for _ in range(n)]
    min_cost[0] = 0
    to = [[] for _ in range(n)]

    for _ in range(n):
        v = -1
        for u in range(n):
            if used[u] == 1:
                continue
            if v == -1 or min_cost[u] < min_cost[v]:
                v = u
        assert v != -1 and min_cost[v] < INF

        used[v] = 1
        if parent[v] != -1:
            p = parent[v]
            w = min_cost[v]
            to[p].append((v, w))
            to[v].append((p, w))

        for u in range(n):
            if used[u] == 0 and cost[v][u] < min_cost[u]:
                min_cost[u] = cost[v][u]
                parent[u] = v

    return to


def example():
    # cost[i][j]: 頂点iと頂点jを結ぶ辺の重み
    cost = [
        [0, 1, 4, 3],
        [1, 0, 2, 5],
        [4, 2, 0, 1],
        [3, 5, 1, 0],
    ]
    to = prim(cost)
    print(to)

    # MSTの合計重み
    total = sum(w for edges in to for _, w in edges) // 2
    print(total)  # 4


if __name__ == '__main__':
    example()
