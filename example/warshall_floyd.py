INF = 10 ** 18

n = 23  # nは頂点数
m = 42  # mは辺数
abc = [[0, 1, 2] for _ in range(m)]  # aからbへの距離cの辺数がm

d = [[INF for _ in range(n)] for _ in range(n)]  # iからjへの最短経路テーブル（初期値はINF）
for i in range(n):
    d[i][i] = 0  # 自分自身への移動は0
for a, b, c in abc:
    d[a][b] = c  # aからbへの直接の距離cを設定
    # d[b][a] = c  # 無効グラフなら必要!!! bからaへの直接の距離cを設定


def warshall_floyd(n):
    for k in range(n):  # kは経由する頂点
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])


warshall_floyd(n)

# 負閉路判定
for i in range(n):
    if d[i][i] < 0:
        print('NEGATIVE CYCLE')
        exit()

# INF判定
for i in range(n):
    for j in range(n):
        if d[i][j] >= INF // 2:
            d[i][j] = 'INF'

print(*d, sep='\n')
