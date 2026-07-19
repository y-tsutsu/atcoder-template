def find_cycles(n, f):
    '''Functional Graphに含まれるすべてのサイクルを頂点列で返す'''
    done = [0 for _ in range(n)]
    ret = []
    for i in range(n):
        if done[i] != 0:
            continue
        p = []
        now = i
        while done[now] == 0:
            done[now] = 1
            p.append(now)
            now = f[now]
        loop = False
        q = []
        for i in p:
            if i == now:
                loop = True
            if loop:
                q.append(i)
                done[i] = 2
        if q:
            ret.append(q)
    return ret
