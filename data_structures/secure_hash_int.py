from random import getrandbits


class SecureHashInt(int):
    _rand = getrandbits(32)

    def __hash__(self):
        return super(SecureHashInt, self).__hash__() ^ SecureHashInt._rand
