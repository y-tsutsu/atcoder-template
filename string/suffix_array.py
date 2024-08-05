from collections import defaultdict


def manber_myers(s, conv=ord):
    n = len(s)
    d = defaultdict(list)
    for i, s in enumerate(s):
        d[conv(s)].append(i)
    rank = [0 for _ in range(n + 1)]
    i = 1
    tbd = []
    for k in sorted(d.keys()):
        for t in d[k]:
            rank[t] = i
        i += len(d[k])
        if len(d[k]) > 1:
            tbd.append(d[k])
    ntbd = []
    w = 1
    while tbd:
        for target in tbd:
            if len(target) == 2:
                x, y = target
                nx = rank[x + w] if x + w < n else -1
                ny = rank[y + w] if y + w < n else -1
                if nx == ny:
                    ntbd.append(target)
                elif nx < ny:
                    rank[y] += 1
                else:
                    rank[x] += 1
                continue
            d = defaultdict(list)
            for t in target:
                nt = rank[t + w] if t + w < n else -1
                d[nt].append(t)
            i = 0
            for k in sorted(d.keys()):
                for t in d[k]:
                    rank[t] += i
                i += len(d[k])
                if len(d[k]) > 1:
                    ntbd.append(d[k])
        tbd, ntbd = ntbd, []
        w *= 2
    result = [0 for _ in range(n + 1)]
    for i, r in enumerate(rank):
        result[r] = i
    return result


def example():
    s = 'missisippi'
    p = manber_myers(s)
    q = [s[i:] for i in p]
    print(*q, sep='\n')


if __name__ == '__main__':
    example()
