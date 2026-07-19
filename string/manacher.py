class Manacher:
    '''文字列中の回文情報をO(n)で構築し、区間の回文判定をO(1)で行う'''

    def __init__(self, s):
        self._s = s
        self._n = len(s)
        self._m = 2 * self._n + 1
        self._r = self._initialize(s)

    def is_palindrome(self, s, e):
        '''部分列[s, e)が回文かを返す'''
        assert 0 <= s <= e <= self._n
        center = s + e
        return e - s < self._r[center]

    def longest_length(self):
        '''最長回文部分列の長さを返す'''
        return max(self._r) - 1

    def longest_range(self):
        '''最長回文部分列の半開区間(s, e)を返す'''
        center = max(range(self._m), key=self._r.__getitem__)
        length = self._r[center] - 1
        return (center - length) // 2, (center + length) // 2

    def longest_palindrome(self):
        '''最長回文部分列を返す'''
        s, e = self.longest_range()
        return self._s[s:e]

    def longest_ranges(self):
        '''同率を含むすべての最長回文部分列の半開区間を返す'''
        length = self.longest_length()
        return [
            ((center - length) // 2, (center + length) // 2)
            for center, r in enumerate(self._r)
            if r - 1 == length
        ]

    def longest_palindromes(self):
        '''同率を含むすべての最長回文部分列を位置ごとに返す'''
        return [self._s[s:e] for s, e in self.longest_ranges()]

    def count(self):
        '''位置の異なる回文部分列の総数を返す'''
        return sum(r // 2 for r in self._r)

    def center_lengths(self):
        '''各文字・文字間を中心とする最長回文部分列の長さを返す'''
        return [r - 1 for r in self._r]

    def judge(self, s, e):
        '''部分列[s, e)が回文かを返す（is_palindromeの別名）'''
        return self.is_palindrome(s, e)

    def max_length(self):
        '''最長回文部分列の長さを返す（longest_lengthの別名）'''
        return self.longest_length()

    def _initialize(self, s):
        ret = [0 for _ in range(self._m)]
        i, j = 0, 0
        while i < self._m:
            while j <= i < self._m - j and self._compare(s, i - j, i + j):
                j += 1
            ret[i] = j
            k = 1
            while k <= i < self._m - k and k + ret[i - k] < j:
                ret[i + k] = ret[i - k]
                k += 1
            i += k
            j -= k
        return ret

    def _compare(self, s, le, ri):
        return s[le // 2] == s[ri // 2] if le & 1 else True


def example():
    s = 'abacxxabba'
    manacher = Manacher(s)

    # 前計算後、任意の区間が回文かをO(1)で判定
    print(manacher.is_palindrome(0, 3))  # True: 'aba'
    print(manacher.is_palindrome(6, 10))  # True: 'abba'
    print(manacher.is_palindrome(0, 4))  # False: 'abac'

    # 最長回文の長さ・区間・実際の文字列
    print(manacher.longest_length())     # 4
    print(manacher.longest_range())      # (6, 10)
    print(manacher.longest_palindrome())  # abba

    # 同率の最長回文が複数あれば、左からすべて取得できる
    tied = Manacher('abacdc')
    print(tied.longest_ranges())          # [(0, 3), (3, 6)]
    print(tied.longest_palindromes())     # ['aba', 'cdc']

    # 同じ文字列でも位置が異なれば別に数える
    print(manacher.count())              # 回文部分文字列の総数

    # 2n+1個の中心について、最長回文の長さを返す
    # 偶数indexは文字間、奇数indexは文字を中心とする
    print(manacher.center_lengths())


if __name__ == '__main__':
    example()
