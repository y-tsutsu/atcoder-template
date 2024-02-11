from sys import maxsize

n = 23  # nは頂点数
m = 42  # mは辺数
abc = [[0, 1, 2] for _ in range(m)]  # aからbへの距離cの辺数がm

INF = maxsize
d = [INF for _ in range(n)]  # iからjへの最短経路テーブル（初期値はINF）
d[0] = 0  # 始点を0で初期化


def bellman_ford(n, d, abc):
    for i in range(n):
        for a, b, c in abc:
            if d[a] <= d[b] + c:
                continue
            d[a] = d[b] + c
            if i == n - 1:
                return False  # 負閉路の検出
    return True
