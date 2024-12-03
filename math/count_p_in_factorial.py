def count_p_in_factorial(n, p):
    '''n!を素数pで割ったときのpの個数を求める'''
    count = 0
    power = p
    while power <= n:
        count += n // power
        power *= p
    return count


def count_p_in_double_factorial(n, p):
    '''n!!を素数pで割ったときのpの個数を求める'''
    if n % 2 == 0:
        m = n // 2
        if p == 2:
            return count_p_in_factorial(m, p) + count_p_in_factorial(m, 2)
        else:
            return count_p_in_factorial(m, p)
    else:
        m = (n + 1) // 2
        return count_p_in_factorial(n, p) - count_p_in_factorial(m - 1, p)
