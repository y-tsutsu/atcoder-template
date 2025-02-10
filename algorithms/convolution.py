def convolution(a, b, mod=998244353, m=23, W=31):
    def _dft(a, w):
        if len(a) == 1:
            return
        n = len(a)
        k = n.bit_length() - 1
        r = 1 << (k - 1)
        for u in w[k:0:-1]:
            for v in range(0, n, 2 * r):
                wi = 1
                for i in range(r):
                    a[v + i], a[v + i + r] = (a[v + i] + a[v + i + r]) % mod, (a[v + i] - a[v + i + r]) * wi % mod
                    wi = wi * u % mod
            r = r // 2

    def _idft(a, iw):
        if len(a) == 1:
            return
        n = len(a)
        k = (n - 1).bit_length()
        r = 1
        for w in iw[1:k + 1]:
            for v in range(0, n, 2 * r):
                wi = 1
                for i in range(r):
                    a[v + i], a[v + i + r] = (a[v + i] + a[v + i + r] * wi) % mod, (a[v + i] - a[v + i + r] * wi) % mod
                    wi = wi * w % mod
            r = r * 2
        ni = pow(n, mod - 2, mod)
        for i in range(n):
            a[i] = a[i] * ni % mod

    w = [pow(W, 2 ** i, mod) for i in range(m, -1, -1)]
    iw = [pow(v, -1, mod) for v in w]
    n = 2 ** (len(a) + len(b) - 2).bit_length()
    a, b = [x % mod for x in a] + [0 for _ in range(n - len(b))], [x % mod for x in b] + [0 for _ in range(n - len(b))]
    _dft(a, w)
    _dft(b, w)
    ret = [(a[i] * b[i]) % mod for i in range(n)]
    _idft(ret, iw)
    return ret
