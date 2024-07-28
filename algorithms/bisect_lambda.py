def bisect(s, e, is_right):
    if not is_right(e):
        return e + 1
    if is_right(s):
        return s
    while e - s > 1:
        m = (e + s) // 2
        if is_right(m):
            e = m
        else:
            s = m
    return e
