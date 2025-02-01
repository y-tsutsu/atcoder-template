from heapq import heappop, heappush


def example():
    hq = []
    def push(x): heappush(hq, x)
    def pop(): return heappop(hq)
    v = 0
    push((v, 0, 0, 0))

    def mypush(v, i, j, k):
        if i == 5 or j == 5 or k == 5:
            return
        push((v, i, j, k))

    while hq:
        v, i, j, k = pop()
        print(v, i, j, k)
        nv = v + 1
        # この条件で次のindexをpushするようにすると，setで重複チェックする必要なく順にindexを進めることができる
        if j == 0 and k == 0:
            mypush(nv, i + 1, j, k)
        if k == 0:
            mypush(nv, i, j + 1, k)
        mypush(nv, i, j, k + 1)


if __name__ == '__main__':
    example()
