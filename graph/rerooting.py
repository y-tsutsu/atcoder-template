class Rerooting:
    '''全方位木DP'''
    def __init__(self, n, e, merge, finish, lift):
        self.n = n
        self.e = e
        self.merge = merge
        self.finish = finish
        self.lift = lift
        self.to = [[] for _ in range(n)]

    def add(self, u, v, data=None):
        self.to[u].append((v, data))
        self.to[v].append((u, data))

    def solve(self, root=0):
        parent = [-1 for _ in range(self.n)]
        order = [root]
        for v in order:
            for to, _ in self.to[v]:
                if to == parent[v]:
                    continue
                parent[to] = v
                order.append(to)

        # dp_down[v]:
        # v を根とする部分木だけ見た Vertex DP
        dp_down = [self.e for _ in range(self.n)]
        for v in reversed(order):
            acc = self.e
            for to, data in self.to[v]:
                if to == parent[v]:
                    continue
                acc = self.merge(acc, self.lift(dp_down[to], data))
            dp_down[v] = self.finish(acc, v)

        # from_parent[v]:
        # 親側から v に届く Edge DP
        from_parent = [self.e for _ in range(self.n)]
        ans = [None for _ in range(self.n)]
        for v in order:
            deg = len(self.to[v])
            # vals[i]:
            # g[v][i] 方向から v に届く Edge DP
            vals = [self.e for _ in range(deg)]
            for i, (to, data) in enumerate(self.to[v]):
                if to == parent[v]:
                    vals[i] = from_parent[v]
                else:
                    vals[i] = self.lift(dp_down[to], data)
            prefix = [self.e for _ in range(deg + 1)]
            suffix = [self.e for _ in range(deg + 1)]
            for i in range(deg):
                prefix[i + 1] = self.merge(prefix[i], vals[i])
            for i in range(deg - 1, -1, -1):
                suffix[i] = self.merge(vals[i], suffix[i + 1])
            # 全方向を見た v の答え
            ans[v] = self.finish(prefix[deg], v)
            # 子へ「その子以外の全方向」を渡す
            for i, (to, data) in enumerate(self.to[v]):
                if to == parent[v]:
                    continue
                without_to = self.merge(prefix[i], suffix[i + 1])
                from_parent[to] = self.lift(self.finish(without_to, v), data)
        return ans


def example0():
    '''各頂点から最遠点までの距離'''
    n = 100
    e = -(1 << 62)

    def merge(a, b): return max(a, b)
    def finish(x, v): return max(x, 0)
    def lift(x, data): return x + 1

    rr = Rerooting(n, e, merge, finish, lift)

    for _ in range(n - 1):
        u, v = 0, 1
        rr.add(u, v)

    ans = rr.solve()
    print(*ans, sep="\n")


def example1():
    '''各頂点から全頂点への距離和'''
    n = 100
    e = (0, 0)  # (距離和, 頂点数)

    def merge(a, b):
        return (a[0] + b[0], a[1] + b[1])

    def finish(x, v):
        dist_sum, size = x
        return (dist_sum, size + 1)

    def lift(x, data):
        dist_sum, size = x
        return (dist_sum + size, size)

    rr = Rerooting(n, e, merge, finish, lift)

    for _ in range(n - 1):
        u, v = 0, 1
        rr.add(u, v)

    ans = rr.solve()
    for dist_sum, size in ans:
        print(dist_sum)


def example2():
    '''重み付き木の最遠距離'''
    n = 100
    e = -(1 << 62)

    def merge(a, b): return max(a, b)
    def finish(x, v): return max(x, 0)
    def lift(x, data): return x + data

    rr = Rerooting(n, e, merge, finish, lift)

    for _ in range(n - 1):
        u, v, w = 0, 1, 10
        rr.add(u, v, w)

    ans = rr.solve()
    print(*ans, sep="\n")


if __name__ == '__main__':
    example0()
