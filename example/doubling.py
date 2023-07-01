MAX = 64


def doubling(a):
    n = len(a)
    d = [a[:]]
    for _ in range(MAX - 1):
        p = [0 for _ in range(n)]
        for i in range(n):
            p[i] = d[-1][d[-1][i]]
        d.append(p)
    return d


def query(pos, n, d):
    '''posをn回移動する'''
    for i in range(MAX - 1, -1, -1):
        if n >> i & 1 == 0:
            continue
        pos = d[i][pos]
    return pos
