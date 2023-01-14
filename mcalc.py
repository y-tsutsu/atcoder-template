def mpow(base, exp, mod):
    return pow(base, exp, mod)  # 標準関数でmod対応されている


def mdiv(n, r, mod):
    return (n * pow(r, mod - 2, mod)) % mod


def mcomb(n, r, mod):
    if r > n:
        return 0
    ret = 1
    for i in range(r):
        ret *= n - i
        ret *= pow(i + 1, mod - 2, mod)
        ret %= mod
    return ret


def mcombr(n, r, mod):
    return mcomb(n + r - 1, r, mod)


def maccumulate(a, mod):
    ret = a[:]
    for i in range(len(a) - 1):
        ret[i + 1] += ret[i]
        ret[i + 1] %= mod
    return ret
