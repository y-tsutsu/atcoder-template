from functools import cmp_to_key
from math import isqrt


def mo(xy, q, n):
    '''区間をMo's algorithmで処理する順番に並べる

    xy: 半開区間[l, r)のリスト
    q: クエリ数
    n: 配列の長さ
    戻り値: (元のクエリ番号, (l, r))のリスト

    lを幅n/sqrt(q)程度のブロックに分け、ブロックごとにrを
    昇順・降順へ交互に並べることで、区間端点の総移動量を抑える。
    '''
    if q == 0:
        return []
    w = max(1, n // isqrt(q))
    e = [x // w for x, y in xy]
    p = [(i, (x, y)) for i, (x, y) in enumerate(xy)]

    def cmp(u, v):
        i, (a, b) = u
        j, (c, d) = v
        if e[i] < e[j]:
            return -1
        if e[i] > e[j]:
            return 1
        if e[i] % 2 == 0:
            if b < d:
                return -1
            if b > d:
                return 1
        else:
            if b < d:
                return 1
            if b > d:
                return -1
        return 0

    p.sort(key=cmp_to_key(cmp))
    return p


def example():
    # 区間クエリを、現在の区間から少ない変更で移動できる順に並べる
    queries = [(0, 5), (3, 8), (1, 4), (6, 10)]
    for query_id, (l, r) in mo(queries, len(queries), 10):
        print(query_id, l, r)

    # 二次元の点も、xをブロック分割してy方向へ蛇行する順に並べられる
    # 座標の上限Wをn、点の個数をqとして渡す
    points = [(1, 8), (7, 2), (4, 5), (9, 9)]
    order = mo(points, len(points), 10)
    print([point_id for point_id, _ in order])


if __name__ == '__main__':
    example()
