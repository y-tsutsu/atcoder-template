def chunks(a, n):
    return [a[i:i + n] for i in range(0, len(a), n)]


def scatter(a, n):
    return [a[i::n] for i in range(n)]


def rrotate(p):
    h, w = len(p), len(p[0])
    ret = [['' for _ in range(h)] for _ in range(w)]
    for i in range(h):
        for j in range(w):
            ret[j][h - i - 1] = p[i][j]
    return ret


def lrotate(p):
    h, w = len(p), len(p[0])
    ret = [['' for _ in range(h)] for _ in range(w)]
    for i in range(h):
        for j in range(w):
            ret[w - j - 1][i] = p[i][j]
    return ret


def transpose(p):
    return [x for x in zip(*p)]


def normalize(p, empty='.'):
    h, w = len(p), len(p[0])
    mni, mxi, mnj, mxj = h, -1, w, -1
    for i in range(h):
        for j in range(w):
            if p[i][j] == empty:
                continue
            mni, mxi, mnj, mxj = min(mni, i), max(mxi, i), min(mnj, j), max(mxj, j)
    rh, rw = mxi - mni + 1, mxj - mnj + 1
    ret = [[empty for _ in range(rw)] for _ in range(rh)]
    for i in range(h):
        for j in range(w):
            if p[i][j] == empty:
                continue
            ret[i - mni][j - mnj] = p[i][j]
    return ret


def example():
    p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(chunks(p, 3))
    print(scatter(p, 3))

    p = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    print(rrotate(p))
    print(lrotate(p))
    print(transpose(p))

    p = ['....', '###.', '.#..', '....']
    for x in normalize(p):
        print(*x)


if __name__ == '__main__':
    example()
