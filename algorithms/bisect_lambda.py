def bisect_ng_ok(s, e, is_ok):
    if not is_ok(e):
        return e + 1
    if is_ok(s):
        return s
    while e - s > 1:
        m = (e + s) // 2
        if is_ok(m):
            e = m
        else:
            s = m
    return e


def bisect_ok_ng(s, e, is_ok):
    if is_ok(e):
        return e
    if not is_ok(s):
        return s - 1
    while e - s > 1:
        m = (e + s) // 2
        if is_ok(m):
            s = m
        else:
            e = m
    return s
