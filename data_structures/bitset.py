class BitSet:
    def __init__(self, size, negative_index=False, value=0):
        self._min = -size if negative_index else 0
        self._max = size - 1
        self._size = self._max - self._min + 1
        self._value = value & ((1 << self._size) - 1)
        self._negative_index = negative_index

    def _get_arg_size(self):
        return self._size // 2 if self._negative_index else self._size

    def __lshift__(self, shift):
        return BitSet(self._get_arg_size(), self._negative_index, self._value << shift)

    def __rshift__(self, shift):
        return BitSet(self._get_arg_size(), self._negative_index, self._value >> shift)

    def __ilshift__(self, shift):
        self._value = (self._value << shift) & ((1 << self._size) - 1)
        return self

    def __irshift__(self, shift):
        self._value >>= shift
        return self

    def __or__(self, other):
        assert self._size == other._size and self._negative_index == other._negative_index
        return BitSet(self._get_arg_size(), self._negative_index, self._value | other._value)

    def __and__(self, other):
        assert self._size == other._size and self._negative_index == other._negative_index
        return BitSet(self._get_arg_size(), self._negative_index, self._value & other._value)

    def __xor__(self, other):
        assert self._size == other._size and self._negative_index == other._negative_index
        return BitSet(self._get_arg_size(), self._negative_index, self._value ^ other._value)

    def __ior__(self, other):
        assert self._size == other._size and self._negative_index == other._negative_index
        self._value |= other._value
        return self

    def __iand__(self, other):
        assert self._size == other._size and self._negative_index == other._negative_index
        self._value &= other._value
        return self

    def __ixor__(self, other):
        assert self._size == other._size and self._negative_index == other._negative_index
        self._value ^= other._value
        return self

    def __getitem__(self, i):
        assert self._min <= i <= self._max
        return (self._value >> (i - self._min)) & 1

    def __setitem__(self, i, b):
        assert self._min <= i <= self._max and b in (0, 1)
        p = i - self._min
        self._value = (self._value | (1 << p)) if b else (self._value & ~(1 << p))

    def __str__(self):
        return f'{self._value:0{self._size}b}'
