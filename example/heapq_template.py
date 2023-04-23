from heapq import heappop, heappush


def main():
    hq = []
    def push(x): heappush(hq, x)
    def pop(): return heappop(hq)


if __name__ == '__main__':
    main()
