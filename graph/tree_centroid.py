def tree_centroids(n, to, vertex_weights=None):
    '''取り除いた後の各連結成分の重みが全体の半分以下になる頂点を返す'''
    if vertex_weights is None:
        vertex_weights = [1] * n

    parent = [-2] * n
    parent[0] = -1
    order = [0]
    for i in order:
        for j in to[i]:
            if j == parent[i]:
                continue
            parent[j] = i
            order.append(j)

    subtree_weights = vertex_weights[:]
    for i in reversed(order[1:]):
        subtree_weights[parent[i]] += subtree_weights[i]

    total = sum(vertex_weights)
    ret = []
    for i in range(n):
        max_component = total - subtree_weights[i]
        for j in to[i]:
            if parent[j] == i:
                max_component = max(max_component, subtree_weights[j])
        if max_component * 2 <= total:
            ret.append(i)
    return ret


def example():
    # 重心は、取り除いた後にできる各連結成分の頂点数を半分以下にする頂点
    to = [
        [1, 2, 3, 6],
        [0],
        [0],
        [0, 4],
        [3, 5],
        [4],
        [0],
    ]
    print(tree_centroids(7, to))  # [0]

    # 頂点に重みがある場合も同じ関数を使える
    print(tree_centroids(7, to, [1, 1, 1, 10, 1, 1, 1]))  # [3]


if __name__ == '__main__':
    example()
