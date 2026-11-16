from array import array
from bisect import bisect_left


class WaveletMatrix:
    '''更新のない整数列の区間順位・個数を扱う。構築O(N log σ)、クエリO(log σ)'''

    def __init__(self, a):
        self._n = len(a)
        self._values = sorted(set(a))
        self._log = (len(self._values) - 1).bit_length() if a else 0
        ranks = {x: i for i, x in enumerate(self._values)}
        a = [ranks[x] for x in a]
        self._ones = []
        self._zeros = []
        for bit in reversed(range(self._log)):
            prefix = array('I', [0])
            zeros, ones = [], []
            for x in a:
                b = (x >> bit) & 1
                prefix.append(prefix[-1] + b)
                if b:
                    ones.append(x)
                else:
                    zeros.append(x)
            self._ones.append(prefix)
            self._zeros.append(len(zeros))
            a = zeros + ones

    def kth_smallest(self, l, r, k):
        '''a[l:r]の小さい方からk番目を返す（kは0始まり、重複も数える）'''
        assert 0 <= l <= r <= self._n
        assert 0 <= k < r - l
        rank = 0
        for level, bit in enumerate(reversed(range(self._log))):
            prefix = self._ones[level]
            lo, ro = prefix[l], prefix[r]
            zeros = (r - l) - (ro - lo)
            if k < zeros:
                l, r = l - lo, r - ro
            else:
                k -= zeros
                rank |= 1 << bit
                offset = self._zeros[level]
                l, r = offset + lo, offset + ro
        return self._values[rank]

    def kth_largest(self, l, r, k):
        '''a[l:r]の大きい方からk番目を返す（kは0始まり）'''
        return self.kth_smallest(l, r, r - l - 1 - k)

    def count_less(self, l, r, x):
        '''a[l:r]に含まれるx未満の要素数を返す'''
        assert 0 <= l <= r <= self._n
        rank = bisect_left(self._values, x)
        if rank == len(self._values):
            return r - l
        ret = 0
        for level, bit in enumerate(reversed(range(self._log))):
            prefix = self._ones[level]
            lo, ro = prefix[l], prefix[r]
            if (rank >> bit) & 1:
                ret += (r - l) - (ro - lo)
                offset = self._zeros[level]
                l, r = offset + lo, offset + ro
            else:
                l, r = l - lo, r - ro
        return ret

    def range_count(self, l, r, lo, hi):
        '''a[l:r]に含まれるlo以上hi未満の要素数を返す'''
        assert lo <= hi
        return self.count_less(l, r, hi) - self.count_less(l, r, lo)

    def count(self, l, r, x):
        '''a[l:r]に含まれる整数xの個数を返す'''
        return self.range_count(l, r, x, x + 1)

    def prev_value(self, l, r, x):
        '''a[l:r]のx未満の最大値を返す（なければNone）'''
        k = self.count_less(l, r, x)
        return self.kth_smallest(l, r, k - 1) if k else None

    def next_value(self, l, r, x):
        '''a[l:r]のx以上の最小値を返す（なければNone）'''
        k = self.count_less(l, r, x)
        return self.kth_smallest(l, r, k) if k < r - l else None


def example():
    # 元の整数列をそのまま渡せる。負数・大きい値・重複に対応し、座標圧縮は内部で行う
    a = [5, -1, 4, 2, 3, 2]
    wm = WaveletMatrix(a)
    # インデックス区間も値の範囲も半開区間。要素の更新はできない
    print(wm.kth_smallest(1, 6, 2))    # 2: [-1, 2, 2, 3, 4]の0始まり2番目
    print(wm.kth_largest(1, 6, 0))     # 4
    print(wm.count_less(0, 6, 3))      # 3: 3未満
    print(wm.range_count(0, 6, 2, 5))  # 4: 2以上5未満
    print(wm.count(0, 6, 2))           # 2
    print(wm.prev_value(0, 6, 3))      # 2: 3未満の最大値
    print(wm.next_value(0, 6, 3))      # 3: 3以上の最小値（同値も含む）
    print(wm.prev_value(0, 6, -1))     # None
    print(wm.next_value(0, 0, 3))      # None: 空区間


if __name__ == '__main__':
    example()
