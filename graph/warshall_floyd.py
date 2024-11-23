from sys import maxsize

INF = maxsize // 4


def warshall_floyd(n, d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


def exist_negative_cycle(n, d):
    '''負閉路判定'''
    for i in range(n):
        if d[i][i] < 0:
            return True
    return False


def is_disconnected_vertex(d, i, j):
    '''INF判定'''
    return True if d[i][j] >= INF // 2 else False


def update_new_edge(n, d, a, b, c):
    '''辺の追加更新'''
    d[a][b] = min(d[a][b], c)
    d[b][a] = min(d[b][a], c)
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], d[i][a] + d[a][b] + d[b][j])
            d[i][j] = min(d[i][j], d[i][b] + d[b][a] + d[a][j])


def example():
    n = 23  # nは頂点数
    m = 42  # mは辺数
    abc = [[0, 1, 2] for _ in range(m)]  # aからbへの距離cの辺数がm

    d = [[INF for _ in range(n)] for _ in range(n)]  # iからjへの最短経路テーブル（初期値はINF）
    for i in range(n):
        d[i][i] = 0  # 自分自身への移動は0
    for a, b, c in abc:
        d[a][b] = c  # aからbへの直接の距離cを設定
        # d[b][a] = c  # 無向グラフなら必要!!! bからaへの直接の距離cを設定

    warshall_floyd(n, d)
    b = exist_negative_cycle(n, d)
    b = is_disconnected_vertex(d, 0, n - 1)


if __name__ == '__main__':
    example()
