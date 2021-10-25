def recursion(k, value):
    if len(value) == L:
        cnt = 0
        for v in value:
            if v in 'aeiou':
                cnt += 1
        if cnt >= 1 and L - cnt >= 2:
            print(value)
        return

    if k < C:
        recursion(k + 1, value + letters[k])
        recursion(k + 1, value)


L, C = map(int, input().strip().split())
letters = input().strip().split()
letters.sort()

recursion(0, '')
