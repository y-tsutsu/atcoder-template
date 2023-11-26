from collections import Counter, defaultdict


def mpow(base, exp, mod):
    return pow(base, exp, mod)  # 標準関数でmod対応されている


def mpow_of_mpow(a, b, c, mod):
    '''(a ** (b ** c)) % mod'''
    if a % mod == 0:
        return 0
    x = pow(b, c, mod - 1)
    return pow(a, x, mod)


def mdiv(n, r, mod):
    return (n * pow(r, mod - 2, mod)) % mod


def mdiv2(n, r, mod):
    '''modが素数でないバージョン (n / r) % mod => (n % (mod * r)) // r'''
    return (n % (mod * r)) // r


def mcomb(n, r, mod):
    if r > n:
        return 0
    ret = 1
    for i in range(min(r, n - r)):
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


def mgeosum(a, r, n, mod):
    '''等比数列の和のMOD版（a:初項 r:公比 n:項数）'''
    if n == 1:
        return a % mod
    x = sum(a, r, n // 2, mod)
    ret = (x + pow(r, n // 2, mod) * x) % mod
    if n % 2 == 1:
        ret += pow(r, n - 1, mod)
        ret %= mod
    return ret


def mlcm(a, mod):
    '''最小公倍数のMOD版'''
    def prime_factorize(x):
        pass
    p = [Counter(prime_factorize(x)) for x in a]
    d = defaultdict(int)
    for c in p:
        for k, v in c.items():
            d[k] = max(d[k], v)
    ret = 1
    for k, v in d.items():
        ret *= pow(k, v, mod)
        ret %= mod
    return ret
