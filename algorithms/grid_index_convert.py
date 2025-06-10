def ptoi(i, j, w): return i * w + j
def itop(v, w): return v // w, v % w


def pack(i, j, k, mj, mk): return i * mj * mk + j * mk + k
def unpack(v, mj, mk): return v // (mj * mk), (v % (mj * mk)) // mk, (v % (mj * mk)) % mk


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
                x = pack(i, j, k, h, w)
                ii, jj, kk = unpack(x, h, w)
                assert i == ii and j == jj and k == kk
                print(i, j, k, x)


if __name__ == '__main__':
    example()
