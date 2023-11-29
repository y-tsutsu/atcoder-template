def acm2dim(p):
    h, w = len(p), len(p[0])
    q = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    for i in range(h):
        for j in range(w):
            q[i + 1][j + 1] = q[i + 1][j] + p[i][j]
    for j in range(w + 1):
        for i in range(h):
            q[i + 1][j] += q[i][j]
    return q
