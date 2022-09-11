def divisors(n):
    ld, ud = [], []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            ld.append(i)
            if i == n // i:
                continue
            ud.append(n // i)
    return ld + ud[::-1]
