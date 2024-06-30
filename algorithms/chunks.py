def chunks(p, n):
    return [p[i:i + n] for i in range(0, len(p), n)]
