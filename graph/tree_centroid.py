from sys import stdin


_tokens = (y for x in stdin for y in x.split())
def read(): return next(_tokens)
def iread(): return int(next(_tokens))


def recurboost(func=None, stack=[]):
    pass


def main():
    n = iread()
    to = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = iread() - 1, iread() - 1
        to[a].append(b)
        to[b].append(a)
    c = [iread() for _ in range(n)]  # 頂点の重み
    tot = sum(c)
    q = []  # 重心の個数は1 or 2

    @recurboost
    def dfs(i, p):
        ret = c[i]
        mx = 0  # 子側の部分木の重みの最大値
        for j in to[i]:
            if j == p:
                continue
            r = yield dfs(j, i)
            mx = max(mx, r)
            ret += r
        mx = max(mx, tot - ret)  # 親側の部分木の重み（自身の頂点の重みも含む）とのmax
        if mx * 2 <= tot:  # 部分木の重みの2倍がトータルを超えていない頂点が重心
            q.append(i)
        yield ret

    dfs(0, -1)
    print(q)


if __name__ == '__main__':
    main()
