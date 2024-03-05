def floor_sum(n, m, a, b):
    '''(a * i + b) // m (i: [0, n])'''
    ans = 0
    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m
    if b >= m:
        ans += n * (b // m)
        b %= m
    ym = (a * n + b) // m
    xm = ym * m - b
    if ym == 0:
        return ans
    ans += (n - (xm + a - 1) // a) * ym
    ans += floor_sum(ym, a, m, (a - xm % a) % a)
    return ans
