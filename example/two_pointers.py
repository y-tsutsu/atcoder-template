def main():
    '''尺取り法のテンプレート'''

    def ok(ri):
        '''riを適用しても条件を満たすか判定'''
        return True

    def push(ri):
        '''riを適用'''
        pass

    def pop(le):
        '''leを除外'''
        pass

    n = 100
    ans = 0
    ri = 0
    for le in range(n):
        while ri != n and ok(ri):
            push(ri)
            ri += 1
        ans += ri - le
        if le == ri:
            ri += 1
        else:
            pop(le)
    print(ans)


if __name__ == '__main__':
    main()
