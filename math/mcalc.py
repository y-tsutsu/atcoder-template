from collections import Counter, defaultdict


def mpow(base, exp, mod):
    ret = 1
    while exp:
        if exp % 2:
            ret *= base
            ret %= mod
        base *= base
        base %= mod
        exp >>= 1
    return ret


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


class MComb:
    def __init__(self, max_, mod):
        self._mod = mod
        self._fact = [1, 1]
        self._factinv = [1, 1]
        inv = [0, 1]
        for i in range(2, max_ + 1):
            self._fact.append((self._fact[-1] * i) % mod)
            inv.append((-inv[mod % i] * (mod // i)) % mod)
            self._factinv.append((self._factinv[-1] * inv[-1]) % mod)

    def comb(self, n, r):
        if r < 0 or r > n:
            return 0
        r = min(r, n - r)
        return (self._fact[n] * self._factinv[r] * self._factinv[n - r]) % self._mod

    def combr(self, n, r):
        return self.comb(n + r - 1, r)


def maccumulate(a, mod):
    ret = [0] + a
    for i in range(len(a)):
        ret[i + 1] += ret[i]
        ret[i + 1] %= mod
    return ret


def recurboost(func=None, stack=[]):
    pass


@recurboost
def mgeosum(a, r, n, mod):
    '''等比数列の和のMOD版（a:初項 r:公比 n:項数）'''
    if n == 1:
        yield a % mod
    x = yield mgeosum(a, r, n // 2, mod)
    ret = (x + pow(r, n // 2, mod) * x) % mod
    if n % 2 == 1:
        ret = (a + r * ret) % mod
    yield ret


def recurboostmemo(func=None, stack=[], memo={}, args_list=[]):
    pass


@recurboostmemo
def mgeosummemo(a, r, n, mod):
    '''等比数列の和のMODメモ化再帰版（a:初項 r:公比 n:項数）'''
    if n == 1:
        yield a % mod
    u, v = n // 2, (n + 1) // 2
    x = yield mgeosummemo(a, r, u, mod)
    y = yield mgeosummemo(a, r, v, mod)
    y *= pow(r, u, mod)
    yield (x + y) % mod


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
