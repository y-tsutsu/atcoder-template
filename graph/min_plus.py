INF = 1 << 62


def min_plus_mul(a, b):
    '''min-plus行列積を返す'''
    n = len(a)
    ret = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        ri = ret[i]
        for k in range(n):
            aik = a[i][k]
            bk = b[k]
            for j in range(n):
                ri[j] = min(ri[j], aik + bk[j])
    return ret


def min_plus_pow(a, k):
    '''min-plus行列積で行列のk乗を返す'''
    assert k >= 0
    n = len(a)
    ret = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        ret[i][i] = 0
    a = [row[:] for row in a]
    while k:
        if k & 1:
            ret = min_plus_mul(ret, a)
        a = min_plus_mul(a, a)
        k >>= 1
    return ret


def example():
    # cost[i][j]: 頂点iから頂点jへ1回で移動するコスト
    cost = [
        [5, 2, 8],
        [1, 4, 3],
        [6, 2, 7],
    ]

    # dist[i][j]: 頂点iからちょうど10回移動して頂点jへ行く最小コスト
    dist = min_plus_pow(cost, 10)
    print(dist[0][2])

    # ちょうど10回移動して各頂点へ戻る最小コスト
    for i in range(len(cost)):
        print(dist[i][i])


if __name__ == '__main__':
    example()
