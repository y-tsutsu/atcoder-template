def mpow(base, exp, mod):
    a = [1]  # 2のべき乗
    while a[-1] * 2 <= exp:
        a.append(a[-1] * 2)
    b = {1: base % mod}  # x ** 2のべき乗数
    for i in range(len(a) - 1):
        b[a[i + 1]] = (b[a[i]] ** 2) % mod
    c = []  # yを2のべき乗に分解
    for x in a[::-1]:
        if exp >= x:
            c.append(x)
            exp -= x
    ret = 1
    for x in c:
        ret *= b[x]
        ret %= mod
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
