def ptoi(i, j, w): return i * w + j
def itop(i, w): return i // w, i % w


def ptoi3d(i, j, k, h, w): return i * h * w + j * w + k
def itop3d(i, h, w): return i // (h * w), (i % (h * w)) // w, (i % (h * w)) % w


def example():
    d, h, w = 2, 3, 4
    for i in range(h):
        for j in range(w):
            x = ptoi(i, j, w)
            ii, jj = itop(x, w)
            assert i == ii and j == jj
            print(i, j, x)
    for i in range(d):
        for j in range(h):
            for k in range(w):
                x = ptoi3d(i, j, k, h, w)
                ii, jj, kk = itop3d(x, h, w)
                assert i == ii and j == jj and k == kk
                print(i, j, k, x)


if __name__ == '__main__':
    example()
