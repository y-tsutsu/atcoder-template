def round_half_up(n: int, ndigits):
    x = 10 ** ndigits
    return (n + x // 2) // x * x


def round_half_up_float(n: float, ndigits=0):
    return round(n + 0.000000005, ndigits)
