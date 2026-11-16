def find_cycle(n, to):
    '''有向グラフのサイクルを頂点列で返し、存在しなければ空リストを返す'''
    state = [0 for _ in range(n)]  # 0: 未訪問, 1: DFS中, 2: 探索完了
    parent = [-1 for _ in range(n)]

    for start in range(n):
        if state[start] != 0:
            continue
        state[start] = 1
        stack = [(start, 0)]
        while stack:
            v, i = stack[-1]
            if i == len(to[v]):
                state[v] = 2
                stack.pop()
                continue

            u = to[v][i]
            stack[-1] = (v, i + 1)
            if state[u] == 0:
                state[u] = 1
                parent[u] = v
                stack.append((u, 0))
            elif state[u] == 1:
                cycle = [v]
                while cycle[-1] != u:
                    cycle.append(parent[cycle[-1]])
                cycle.reverse()
                return cycle
    return []


def bootstrap(func=None, stack=[]):
    pass


def find_cycle_recursive(n, to):
    '''有向グラフのサイクルを頂点列で返す再帰版（bootstrapを補って使う）'''
    state = [0 for _ in range(n)]  # 0: 未訪問, 1: 現在の探索経路上, 2: 探索完了
    parent = [-1 for _ in range(n)]

    @bootstrap
    def dfs(v):
        state[v] = 1
        for u in to[v]:
            if state[u] == 0:
                parent[u] = v
                cycle = yield dfs(u)
                if cycle:
                    yield cycle
            elif state[u] == 1:
                # 探索経路上の祖先uへ戻る辺。親への辺も除外しない
                cycle = [v]
                while cycle[-1] != u:
                    cycle.append(parent[cycle[-1]])
                cycle.reverse()
                yield cycle
            # 探索完了済みの頂点への辺は、単なる合流なので無視する
        state[v] = 2
        yield []

    for start in range(n):
        if state[start] != 0:
            continue
        cycle = dfs(start)
        if cycle:
            return cycle
    return []


def has_cycle(n, to):
    '''有向グラフにサイクルが存在するかを返す'''
    return bool(find_cycle(n, to))


def example():
    # 0 -> 1 -> 2 -> 0 がサイクル、2 -> 3はサイクル外の辺
    to = [[1], [2], [0, 3], []]
    cycle = find_cycle(4, to)
    print(cycle)             # [0, 1, 2]
    print(has_cycle(4, to))  # True

    # DAGにはサイクルがない
    dag = [[1, 2], [3], [3], []]
    print(find_cycle(4, dag))  # []
    print(has_cycle(4, dag))   # False

    # 再帰版も同じ返り値（使用時は上のbootstrapを実装で置き換える）
    # print(find_cycle_recursive(4, to))  # [0, 1, 2]


if __name__ == '__main__':
    example()
