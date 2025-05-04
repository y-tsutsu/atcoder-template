def int_to_base(n: int, base: int) -> str:
    assert 2 <= base <= 9
    if n == 0:
        return '0'
    p = []
    while n > 0:
        p.append(str(n % base))
        n //= base
    return ''.join(p[::-1])


def base_to_int(s: str, base: int) -> int:
    assert 2 <= base <= 9
    assert all(0 <= int(c) < base for c in s)
    return sum(int(c) * (base ** i) for i, c in enumerate(s[::-1]))
