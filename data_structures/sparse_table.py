class SparseTable:
    '''更新のない配列に対する冪等な区間演算をO(1)で行うSparse Table

    opにはmin、max、gcdなどop(x, x) == xを満たす演算を指定する。
    構築O(n log n)、区間取得O(1)、更新には対応しない。
    '''

    def __init__(self, a, op):
        assert len(a) > 0
        self._n = len(a)
        self._op = op
        self._log = [0 for _ in range(self._n + 1)]
        for i in range(2, self._n + 1):
            self._log[i] = self._log[i >> 1] + 1

        self._table = [list(a)]
        k = 1
        while (1 << k) <= self._n:
            length = 1 << k
            half = length >> 1
            prev = self._table[-1]
            self._table.append([
                op(prev[i], prev[i + half])
                for i in range(self._n - length + 1)
            ])
            k += 1

    def __len__(self):
        '''配列の長さを返す'''
        return self._n

    def prod(self, s, e):
        '''半開区間[s, e)の演算結果を返す'''
        assert 0 <= s < e <= self._n
        k = self._log[e - s]
        return self._op(self._table[k][s], self._table[k][e - (1 << k)])


def example():
    a = [5, 2, 4, 7, 1, 3, 6]

    # 配列が更新されない区間最小値クエリ
    st_min = SparseTable(a, min)
    print(st_min.prod(1, 5))  # 1: min([2, 4, 7, 1])
    print(st_min.prod(2, 4))  # 4: min([4, 7])

    # 冪等な演算ならmaxやgcdにも利用できる
    st_max = SparseTable(a, max)
    print(st_max.prod(1, 5))  # 7


if __name__ == '__main__':
    example()
