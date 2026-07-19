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


if __name__ == '__main__':
    example()
