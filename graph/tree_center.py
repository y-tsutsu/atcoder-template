from collections import deque


def tree_centers(n, to):
    '''各頂点への最大距離を最小にする、直径の中央の頂点を返す'''
    def bfs(s, d, p):
        dq = deque()
        dq.append(s)
        while dq:
            i = dq.popleft()
            for j in to[i]:
                if d[j] != -1:
                    continue
                d[j] = d[i] + 1
                p[j] = i
                dq.append(j)

    d = [-1 for _ in range(n)]
    p = [-1 for _ in range(n)]
    d[0] = 0
    bfs(0, d, p)
    m = max(d)
    s = [i for i, x in enumerate(d) if x == m][0]

    d = [-1 for _ in range(n)]
    p = [-1 for _ in range(n)]
    d[s] = 0
    bfs(s, d, p)
    m = max(d)
    e = [i for i, x in enumerate(d) if x == m][0]

    route = []
    i = e
    while i != -1:
        route.append(i)
        if i == s:
            break
        i = p[i]

    if len(route) % 2 == 1:
        return [route[len(route) // 2]]
    return sorted([route[len(route) // 2 - 1], route[len(route) // 2]])


def example():
    # 中心は直径の中央。直径の辺数が偶数なら1頂点、奇数なら2頂点
    to = [
        [1, 2, 3, 6],
        [0],
        [0],
        [0, 4],
        [3, 5],
        [4],
        [0],
    ]
    print(tree_centers(7, to))  # [3]


if __name__ == '__main__':
    example()
