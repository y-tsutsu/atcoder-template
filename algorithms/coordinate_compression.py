def compress(a, start=1):
    d = {v: i for i, v in enumerate(sorted(set(a)), start=start)}
    return [d[x] for x in a]
