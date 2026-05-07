def recurboost(func=None, stack=[]):
    pass


def find_cycle(n, to):
    done = [0 for _ in range(n)]

    @recurboost
    def dfs(i, route):
        done[i] = 1
        route.add(i)
        for j in to[i]:
            if j in route:
                yield True
            if done[j] == 1:
                continue
            ret = yield dfs(j, route)
            if ret:
                yield True
        route.remove(i)
        yield False

    for i in range(n):
        if done[i] == 1:
            continue
        ret = dfs(i, set())
        if ret:
            return True
    return False
