def bisect(s, e, is_target):
    if not is_target(e):
        return e + 1
    if is_target(s):
        return s
    while e - s > 1:
        m = (e + s) // 2
        if is_target(m):
            e = m
        else:
            s = m
    return e
