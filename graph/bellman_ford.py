# https://atcoder.jp/contests/abc137/tasks/abc137_e

from collections import deque
from sys import maxsize

INF = maxsize


def check_reachable(n, to, ot):
    # 1からnまでの距離だけが気になる場合は，その間の経路以外の部分で負閉路があっても関係ない．1からnまでの経路に存在する頂点を算出する
    d0 = [0 for _ in range(n)]
    d1 = [0 for _ in range(n)]

    def bfs(s, d, to):
        d[s] = 1
        dq = deque()
        dq.append(s)
        while dq:
            i = dq.popleft()
            for j in to[i]:
                if d[j] == 1:
                    continue
                d[j] = 1
                dq.append(j)
        return d

    bfs(0, d0, to)
    bfs(n - 1, d1, ot)
    ret = [1 if u and v else 0 for u, v in zip(d0, d1)]
    return ret


def bellman_ford(n, d, abc, reachable=None):
    for _ in range(n - 1):
        for a, b, c in abc:
            if d[a] == INF:
                continue
            if d[b] <= d[a] + c:
                continue
            if (reachable is not None) and (reachable[a] == 0 or reachable[b] == 0):
                continue
            d[b] = d[a] + c
    ret = True  # 負閉路の検出
    for _ in range(n - 1):
        for a, b, c in abc:
            if d[a] == INF:
                continue
            if d[b] <= d[a] + c:
                continue
            if (reachable is not None) and (reachable[a] == 0 or reachable[b] == 0):
                continue
            d[b] = -INF  # 負閉路
            ret = False
    return ret


def main():
    n = 23  # nは頂点数
    m = 42  # mは辺数
    abc = [[0, 1, 2] for _ in range(m)]  # aからbへの距離cの辺数がm
    # ベルマンフォードで最長経路を求めたい場合はコストをマイナスにすることで算出できる

    to = [[] for _ in range(n)]
    ot = [[] for _ in range(n)]
    for a, b, _ in abc:
        to[a].append(b)
        ot[b].append(a)
    reachable = check_reachable(n, to, ot)  # 1からnまでの距離のみが気になる場合はreachableを算出して関係ない頂点を除外する

    d = [INF for i in range(n)]  # 0からiへの最短経路テーブル（初期値はINF）
    d[0] = 0  # 始点を0で初期化
    ret = bellman_ford(n, d, abc, reachable)
    if ret:
        print(*d)  # 1からiへの最短経路テーブル（到達できない頂点はINF）
    else:
        print(*d)  # 1からiへの最短経路テーブル（負閉路内の頂点は-INF）


if __name__ == '__main__':
    main()
