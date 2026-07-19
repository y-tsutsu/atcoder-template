class SuffixArray:
    '''接尾辞を辞書順に並べ、部分文字列検索やLCPの計算を行うSuffix Array

    sa[k]: 辞書順でk番目の接尾辞の開始位置
    rank[i]: s[i:]が辞書順で何番目か
    lcp[k]: s[sa[k]:]とs[sa[k + 1]:]のLCPの長さ
    構築O(n log^2 n)、部分文字列検索O(|pattern| log n)、接尾辞LCP取得O(log n)
    '''

    def __init__(self, s):
        self.s = s
        self.n = len(s)
        self.sa = self._build_suffix_array()
        self.rank = [0 for _ in range(self.n)]
        for i, p in enumerate(self.sa):
            self.rank[p] = i
        self.lcp = self._build_lcp_array()
        self._build_lcp_segment_tree()

    def __len__(self):
        '''接尾辞の個数を返す'''
        return self.n

    def __getitem__(self, i):
        '''辞書順でi番目の接尾辞の開始位置を返す'''
        return self.sa[i]

    def search(self, pattern):
        '''patternがprefixとなる接尾辞のSuffix Array上の半開区間を返す'''
        le, ri = 0, self.n
        while le < ri:
            m = (le + ri) // 2
            if self._compare(self.sa[m], pattern) < 0:
                le = m + 1
            else:
                ri = m
        lower = le

        le, ri = lower, self.n
        while le < ri:
            m = (le + ri) // 2
            if self._compare(self.sa[m], pattern) <= 0:
                le = m + 1
            else:
                ri = m
        return lower, le

    def contains(self, pattern):
        '''patternが部分文字列として存在するかを返す'''
        le, ri = self.search(pattern)
        return le < ri

    def count(self, pattern):
        '''patternが部分文字列として出現する回数を返す'''
        le, ri = self.search(pattern)
        return ri - le

    def positions(self, pattern):
        '''patternが出現する開始位置を昇順で返す'''
        le, ri = self.search(pattern)
        return sorted(self.sa[le:ri])

    def lcp_suffix(self, i, j):
        '''s[i:]とs[j:]のLCPの長さを返す'''
        assert 0 <= i < self.n and 0 <= j < self.n
        if i == j:
            return self.n - i
        le, ri = self.rank[i], self.rank[j]
        if le > ri:
            le, ri = ri, le
        return self._lcp_prod(le, ri)

    def distinct_substrings(self):
        '''異なる空でない部分文字列の個数を返す'''
        return self.n * (self.n + 1) // 2 - sum(self.lcp)

    def longest_repeated_substring(self):
        '''2回以上出現する最長の部分文字列を返す'''
        if not self.lcp:
            return ''
        length = max(self.lcp)
        if length == 0:
            return ''
        i = self.lcp.index(length)
        return self.s[self.sa[i]:self.sa[i] + length]

    def _build_suffix_array(self):
        if self.n == 0:
            return []
        sa = list(range(self.n))
        rank = [ord(c) for c in self.s]
        k = 1
        while k < self.n:
            sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < self.n else -1))
            new_rank = [0 for _ in range(self.n)]
            for i in range(1, self.n):
                x, y = sa[i - 1], sa[i]
                key_x = rank[x], rank[x + k] if x + k < self.n else -1
                key_y = rank[y], rank[y + k] if y + k < self.n else -1
                new_rank[y] = new_rank[x] + (key_x < key_y)
            rank = new_rank
            if rank[sa[-1]] == self.n - 1:
                break
            k <<= 1
        return sa

    def _build_lcp_array(self):
        if self.n <= 1:
            return []
        lcp = [0 for _ in range(self.n - 1)]
        h = 0
        for i in range(self.n):
            r = self.rank[i]
            if r == self.n - 1:
                h = 0
                continue
            j = self.sa[r + 1]
            while i + h < self.n and j + h < self.n and self.s[i + h] == self.s[j + h]:
                h += 1
            lcp[r] = h
            if h > 0:
                h -= 1
        return lcp

    def _build_lcp_segment_tree(self):
        self._size = 1 << (max(1, len(self.lcp)) - 1).bit_length()
        self._lcp_tree = [self.n for _ in range(self._size << 1)]
        for i, x in enumerate(self.lcp):
            self._lcp_tree[self._size + i] = x
        for i in range(self._size - 1, 0, -1):
            self._lcp_tree[i] = min(self._lcp_tree[i << 1], self._lcp_tree[i << 1 | 1])

    def _lcp_prod(self, le, ri):
        ret = self.n
        le += self._size
        ri += self._size
        while le < ri:
            if le & 1:
                ret = min(ret, self._lcp_tree[le])
                le += 1
            if ri & 1:
                ri -= 1
                ret = min(ret, self._lcp_tree[ri])
            le >>= 1
            ri >>= 1
        return ret

    def _compare(self, pos, pattern):
        length = min(self.n - pos, len(pattern))
        for i in range(length):
            if self.s[pos + i] < pattern[i]:
                return -1
            if self.s[pos + i] > pattern[i]:
                return 1
        if len(pattern) <= self.n - pos:
            return 0
        return -1


def longest_common_substring(s, t):
    '''sとtの両方に出現する最長の連続部分文字列を返す'''
    used = set(s) | set(t)
    code = 0
    while chr(code) in used:
        code += 1
    separator = chr(code)

    u = s + separator + t
    suffix_array = SuffixArray(u)

    def owner(i):
        if i < len(s):
            return 0
        if i == len(s):
            return -1
        return 1

    length = 0
    pos = 0
    for k, lcp in enumerate(suffix_array.lcp):
        i = suffix_array.sa[k]
        j = suffix_array.sa[k + 1]
        oi, oj = owner(i), owner(j)
        if oi >= 0 and oj >= 0 and oi != oj and length < lcp:
            length = lcp
            pos = i if oi == 0 else j
    return s[pos:pos + length]


def example():
    s = 'banana'
    suffix_array = SuffixArray(s)

    # sa[i]は辞書順でi番目の接尾辞の開始位置
    print(suffix_array.sa)              # [5, 3, 1, 0, 4, 2]
    print([s[i:] for i in suffix_array.sa])
    # ['a', 'ana', 'anana', 'banana', 'na', 'nana']
    print(suffix_array.rank[1])         # 2: s[1:]='anana'は辞書順で2番目
    print(len(suffix_array))            # 6
    print(suffix_array[0])              # 5: 辞書順最小の接尾辞はs[5:]='a'

    # lcp[i]はsa[i]とsa[i + 1]の接尾辞が共有するprefixの長さ
    print(suffix_array.lcp)             # [1, 3, 0, 0, 2]
    print(suffix_array.lcp_suffix(1, 3))  # 3: 'anana'と'ana'のLCPは'ana'

    # 部分文字列の存在判定・出現回数・出現位置
    print(suffix_array.contains('ana'))   # True
    print(suffix_array.count('ana'))      # 2
    print(suffix_array.positions('ana'))  # [1, 3]
    print(suffix_array.search('ana'))     # (1, 3): Suffix Array上の出現範囲

    # Suffix ArrayとLCP配列を利用した代表的な計算
    print(suffix_array.distinct_substrings())         # 15
    print(suffix_array.longest_repeated_substring())  # ana

    # 2つの文字列を連結し、異なる文字列由来の接尾辞間のLCPを調べる
    print(longest_common_substring('abcde', 'cdef'))  # cde


if __name__ == '__main__':
    example()
