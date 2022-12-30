def compression(a):
    d = {v: i for i, v in enumerate(sorted(set(a)), start=1)}
    return [d[x] for x in a]
