def mpow(base, exp, mod):
    if exp == 0:
        return 1
    a = [i for i, x in enumerate(f'{exp:b}'[::-1]) if x == '1']
    i, j, p, ret = 1, 0, base, 1
    if a[0] == 0:
        j += 1
        ret *= base
        ret %= mod
    while j < len(a):
        p = (p ** 2) % mod
        if i == a[j]:
            ret *= p
            ret %= mod
            j += 1
        i += 1
    return ret


def mcomb(n, r, mod):
    if r > n:
        return 0
    ret = 1
    for i in range(r):
        ret *= n - i
        ret *= mpow(i + 1, mod - 2, mod)
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
