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


def can_reach_target(n, f, target):
    '''各頂点からtarget[v]が真の頂点へ到達できるかを返す'''
    state = [0 for _ in range(n)]  # 0: 未訪問、1: 探索中、2: 判定済み
    ret = [False for _ in range(n)]
    for v in range(n):
        if target[v]:
            state[v] = 2
            ret[v] = True

    for start in range(n):
        if state[start] != 0:
            continue

        path = []
        v = start
        while state[v] == 0:
            state[v] = 1
            path.append(v)
            v = f[v]

        # 探索中の頂点へ戻った場合は、targetを含まないサイクルに入った
        reachable = False if state[v] == 1 else ret[v]
        for v in reversed(path):
            state[v] = 2
            ret[v] = reachable
    return ret


def example():
    # find_cycles(): Functional Graphに含まれるサイクルを列挙する
    f = [1, 2, 0, 4, 3, 2, 5]
    print(find_cycles(7, f))  # [[0, 1, 2], [3, 4]]

    # can_reach_target(): 各頂点から目的の頂点集合へ到達できるか判定する
    target = [False, True, False, False, False, False, False]
    print(can_reach_target(7, f, target))
    # [True, True, True, False, False, True, True]

    # ABC446 E: (x, y)を頂点x * m + yとしてFunctional Graphを作る
    m, a, b = 4, 1, 2
    f = [0 for _ in range(m * m)]
    target = [False for _ in range(m * m)]
    for x in range(m):
        for y in range(m):
            v = x * m + y
            z = (a * y + b * x) % m
            f[v] = y * m + z
            target[v] = x == 0 or y == 0
    can_reach_zero = can_reach_target(m * m, f, target)
    print(can_reach_zero.count(False))  # 7


if __name__ == '__main__':
    example()
