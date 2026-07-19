from random import randint


class RollingHash:
    '''部分文字列の比較・LCP・回文判定を高速に行うRolling Hash'''

    def __init__(self, s, mod=952149973289264689, base=randint(256, 1 << 30)):
        self._str = s
        self._n = len(s)
        self._mod = mod
        self._base = base
        self._pow = [1 for _ in range(self._n + 1)]
        for i in range(self._n):
            self._pow[i + 1] = self._pow[i] * base % mod
        self._hash = self._build_hash(s)
        self._reverse_hash = self._build_hash(s[::-1])

    def get_hash(self, s, e):
        '''部分文字列[s, e)のハッシュ値を返す'''
        return self._get_hash(self._hash, s, e)

    def get_reverse_hash(self, s, e):
        '''部分文字列[s, e)を反転したハッシュ値を返す'''
        return self._get_hash(self._reverse_hash, self._n - e, self._n - s)

    def equal(self, s1, e1, s2, e2):
        '''二つの部分文字列が等しいかをハッシュで判定する'''
        return e1 - s1 == e2 - s2 and self.get_hash(s1, e1) == self.get_hash(s2, e2)

    def lcp(self, i, j, max_length=None):
        '''s[i:]とs[j:]のLCPの長さを返す'''
        if max_length is None:
            max_length = min(self._n - i, self._n - j)
        else:
            max_length = min(max_length, self._n - i, self._n - j)
        ok, ng = 0, max_length + 1
        while ng - ok > 1:
            m = (ok + ng) // 2
            if self.equal(i, i + m, j, j + m):
                ok = m
            else:
                ng = m
        return ok

    def is_palindrome(self, s, e):
        '''部分文字列[s, e)が回文かをハッシュで判定する'''
        return self.get_hash(s, e) == self.get_reverse_hash(s, e)

    def _build_hash(self, text):
        h = [0]
        for i, c in enumerate(text):
            x = (self._base * h[i] + ord(c) + 1) % self._mod
            h.append(x)
        return h

    def _get_hash(self, h, s, e):
        return (h[e] - h[s] * self._pow[e - s]) % self._mod


class SegTree:
    pass


class SegRollingHash:
    '''一文字更新に対応したSegment Tree版Rolling Hash'''

    def __init__(self, s, mod=952149973289264689, base=randint(256, 1 << 30)):
        self._mod = mod
        self._base = base
        self._n = len(s)
        self._pow = [1]
        for _ in range(self._n):
            self._pow.append(self._pow[-1] * base % self._mod)
        self._st = self._init_hash(s)

    def _init_hash(self, s):
        def op(x, y):
            hx, rx, lx = x
            hy, ry, ly = y
            h = (hx * self._pow[ly] + hy) % self._mod
            r = (ry * self._pow[lx] + rx) % self._mod
            return h, r, lx + ly

        def e(): return (0, 0, 0)

        v = [(ord(c) + 1, ord(c) + 1, 1) for c in s]
        return SegTree(op, e, self._n, v)

    def get_hash(self, s, e):
        '''部分文字列[s, e)のハッシュ値を返す'''
        return self._st.prod(s, e)[0]

    def get_reverse_hash(self, s, e):
        '''部分文字列[s, e)を反転したハッシュ値を返す'''
        return self._st.prod(s, e)[1]

    def equal(self, s1, e1, s2, e2):
        '''二つの部分文字列が等しいかをハッシュで判定する'''
        return e1 - s1 == e2 - s2 and self.get_hash(s1, e1) == self.get_hash(s2, e2)

    def lcp(self, i, j, max_length=None):
        '''s[i:]とs[j:]のLCPの長さを返す'''
        if max_length is None:
            max_length = min(self._n - i, self._n - j)
        else:
            max_length = min(max_length, self._n - i, self._n - j)
        ok, ng = 0, max_length + 1
        while ng - ok > 1:
            m = (ok + ng) // 2
            if self.equal(i, i + m, j, j + m):
                ok = m
            else:
                ng = m
        return ok

    def is_palindrome(self, s, e):
        '''部分文字列[s, e)が回文かをハッシュで判定する'''
        h, r, _ = self._st.prod(s, e)
        return h == r

    def set(self, p, c):
        '''p番目の文字をcへ更新する'''
        v = ord(c) + 1
        self._st.set(p, (v, v, 1))


def example():
    s = 'abracadabra'
    rh = RollingHash(s)

    # 部分文字列のハッシュをO(1)で取得
    print(rh.get_hash(0, 4))
    print(rh.get_reverse_hash(0, 4))

    # s[0:4]とs[7:11]はどちらも'abra'
    print(rh.equal(0, 4, 7, 11))       # True

    # s[0:]='abracadabra'とs[7:]='abra'のLCPは'abra'
    print(rh.lcp(0, 7))                # 4
    print(rh.lcp(0, 7, 3))             # 3（調べる長さを3文字に制限）

    print(rh.is_palindrome(3, 6))      # True: 'aca'
    print(rh.is_palindrome(0, 4))      # False: 'abra'


def example_seg():
    s = 'abracadabra'

    # Segment Tree版は同じ機能に加えて一文字更新が可能
    srh = SegRollingHash(s)
    print(srh.equal(0, 4, 7, 11))      # True
    print(srh.lcp(0, 7))               # 4
    print(srh.is_palindrome(3, 6))     # True: 'aca'
    srh.set(5, 'x')
    print(srh.is_palindrome(3, 6))     # False: 'acx'


if __name__ == '__main__':
    example()
