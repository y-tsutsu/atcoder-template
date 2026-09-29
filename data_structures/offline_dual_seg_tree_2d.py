class OfflineDualSegTree2D:
    def __init__(self, op, e, h, w):
        self._h = h
        self._w = w
        self._op = op
        self._e = e
        self._log_h = (h - 1).bit_length()
        self._log_w = (w - 1).bit_length()
        self._size_h = 1 << self._log_h
        self._size_w = 1 << self._log_w
        self._d = [[e()] * (self._size_w << 1) for _ in range(self._size_h << 1)]

    def apply(self, si, sj, ei, ej, x):
        si += self._size_h
        ei += self._size_h
        sj0 = sj + self._size_w
        ej0 = ej + self._size_w
        d = self._d
        op = self._op

        while si < ei:
            if si & 1:
                self._apply_w(d[si], sj0, ej0, x, op)
                si += 1
            if ei & 1:
                ei -= 1
                self._apply_w(d[ei], sj0, ej0, x, op)
            si >>= 1
            ei >>= 1

    def _apply_w(self, row, sj, ej, x, op):
        while sj < ej:
            if sj & 1:
                row[sj] = op(row[sj], x)
                sj += 1
            if ej & 1:
                ej -= 1
                row[ej] = op(row[ej], x)
            sj >>= 1
            ej >>= 1

    def _push_w(self, row, k):
        row[k << 1] = self._op(row[k << 1], row[k])
        row[k << 1 | 1] = self._op(row[k << 1 | 1], row[k])
        row[k] = self._e()

    def _push_w_path(self, row, k):
        for i in range(self._log_w, 0, -1):
            self._push_w(row, k >> i)

    def _push_h_point(self, k, j):
        row = self._d[k]
        self._push_w_path(row, j)
        self._d[k << 1][j] = self._op(self._d[k << 1][j], row[j])
        self._d[k << 1 | 1][j] = self._op(self._d[k << 1 | 1][j], row[j])
        row[j] = self._e()

    def set(self, i, j, x):
        i += self._size_h
        j += self._size_w
        for k in range(self._log_h, 0, -1):
            self._push_h_point(i >> k, j)
        row = self._d[i]
        self._push_w_path(row, j)
        row[j] = x

    def build(self):
        d = self._d
        op = self._op
        size_h = self._size_h
        size_w = self._size_w
        h = self._h
        w = self._w
        w2 = size_w << 1

        for i in range(1, size_h):
            row = d[i]
            left = d[i << 1]
            right = d[i << 1 | 1]
            for j in range(w2):
                x = row[j]
                left[j] = op(left[j], x)
                right[j] = op(right[j], x)

        for i in range(size_h, size_h + h):
            row = d[i]
            for j in range(1, size_w):
                x = row[j]
                lj = j << 1
                rj = lj | 1
                row[lj] = op(row[lj], x)
                row[rj] = op(row[rj], x)

        return [d[size_h + i][size_w:size_w + w] for i in range(h)]


class OfflineDualSegTree2DMax:
    def __init__(self, h, w, e=-(1 << 62)):
        self._h = h
        self._w = w
        self._e = e
        self._log_h = (h - 1).bit_length()
        self._log_w = (w - 1).bit_length()
        self._size_h = 1 << self._log_h
        self._size_w = 1 << self._log_w
        self._d = [[e] * (self._size_w << 1) for _ in range(self._size_h << 1)]

    def apply(self, si, sj, ei, ej, x):
        si += self._size_h
        ei += self._size_h
        sj0 = sj + self._size_w
        ej0 = ej + self._size_w
        d = self._d
        while si < ei:
            if si & 1:
                self._apply_w(d[si], sj0, ej0, x)
                si += 1
            if ei & 1:
                ei -= 1
                self._apply_w(d[ei], sj0, ej0, x)
            si >>= 1
            ei >>= 1

    def _apply_w(self, row, sj, ej, x):
        while sj < ej:
            if sj & 1:
                if row[sj] < x:
                    row[sj] = x
                sj += 1
            if ej & 1:
                ej -= 1
                if row[ej] < x:
                    row[ej] = x
            sj >>= 1
            ej >>= 1

    def _push_w(self, row, k):
        x = row[k]
        if row[k << 1] < x:
            row[k << 1] = x
        if row[k << 1 | 1] < x:
            row[k << 1 | 1] = x
        row[k] = self._e

    def _push_w_path(self, row, k):
        for i in range(self._log_w, 0, -1):
            self._push_w(row, k >> i)

    def _push_h_point(self, k, j):
        row = self._d[k]
        self._push_w_path(row, j)
        x = row[j]
        if self._d[k << 1][j] < x:
            self._d[k << 1][j] = x
        if self._d[k << 1 | 1][j] < x:
            self._d[k << 1 | 1][j] = x
        row[j] = self._e

    def set(self, i, j, x):
        i += self._size_h
        j += self._size_w
        for k in range(self._log_h, 0, -1):
            self._push_h_point(i >> k, j)
        row = self._d[i]
        self._push_w_path(row, j)
        row[j] = x

    def build(self):
        d = self._d
        size_h = self._size_h
        size_w = self._size_w
        w2 = size_w << 1
        for i in range(1, size_h):
            row = d[i]
            left = d[i << 1]
            right = d[i << 1 | 1]
            for j in range(w2):
                x = row[j]
                if left[j] < x:
                    left[j] = x
                if right[j] < x:
                    right[j] = x
        for i in range(size_h, size_h + self._h):
            row = d[i]
            for j in range(1, size_w):
                x = row[j]
                lj = j << 1
                rj = lj | 1
                if row[lj] < x:
                    row[lj] = x
                if row[rj] < x:
                    row[rj] = x
        return [d[size_h + i][size_w:size_w + self._w] for i in range(self._h)]


class OfflineDualSegTree2DMin:
    def __init__(self, h, w, e=1 << 62):
        self._h = h
        self._w = w
        self._e = e
        self._log_h = (h - 1).bit_length()
        self._log_w = (w - 1).bit_length()
        self._size_h = 1 << self._log_h
        self._size_w = 1 << self._log_w
        self._d = [[e] * (self._size_w << 1) for _ in range(self._size_h << 1)]

    def apply(self, si, sj, ei, ej, x):
        si += self._size_h
        ei += self._size_h
        sj0 = sj + self._size_w
        ej0 = ej + self._size_w
        d = self._d
        while si < ei:
            if si & 1:
                self._apply_w(d[si], sj0, ej0, x)
                si += 1
            if ei & 1:
                ei -= 1
                self._apply_w(d[ei], sj0, ej0, x)
            si >>= 1
            ei >>= 1

    def _apply_w(self, row, sj, ej, x):
        while sj < ej:
            if sj & 1:
                if row[sj] > x:
                    row[sj] = x
                sj += 1
            if ej & 1:
                ej -= 1
                if row[ej] > x:
                    row[ej] = x
            sj >>= 1
            ej >>= 1

    def _push_w(self, row, k):
        x = row[k]
        if row[k << 1] > x:
            row[k << 1] = x
        if row[k << 1 | 1] > x:
            row[k << 1 | 1] = x
        row[k] = self._e

    def _push_w_path(self, row, k):
        for i in range(self._log_w, 0, -1):
            self._push_w(row, k >> i)

    def _push_h_point(self, k, j):
        row = self._d[k]
        self._push_w_path(row, j)
        x = row[j]
        if self._d[k << 1][j] > x:
            self._d[k << 1][j] = x
        if self._d[k << 1 | 1][j] > x:
            self._d[k << 1 | 1][j] = x
        row[j] = self._e

    def set(self, i, j, x):
        i += self._size_h
        j += self._size_w
        for k in range(self._log_h, 0, -1):
            self._push_h_point(i >> k, j)
        row = self._d[i]
        self._push_w_path(row, j)
        row[j] = x

    def build(self):
        d = self._d
        size_h = self._size_h
        size_w = self._size_w
        w2 = size_w << 1
        for i in range(1, size_h):
            row = d[i]
            left = d[i << 1]
            right = d[i << 1 | 1]
            for j in range(w2):
                x = row[j]
                if left[j] > x:
                    left[j] = x
                if right[j] > x:
                    right[j] = x
        for i in range(size_h, size_h + self._h):
            row = d[i]
            for j in range(1, size_w):
                x = row[j]
                lj = j << 1
                rj = lj | 1
                if row[lj] > x:
                    row[lj] = x
                if row[rj] > x:
                    row[rj] = x
        return [d[size_h + i][size_w:size_w + self._w] for i in range(self._h)]


def example():
    def op(x, y): return max(x, y)
    def e(): return 0
    st = OfflineDualSegTree2D(op, e, 10, 10)
    st.apply(1, 2, 6, 7, 7)
    st.apply(4, 4, 9, 8, 5)
    p = st.build()
    for x in p:
        print(*x)


if __name__ == '__main__':
    example()
