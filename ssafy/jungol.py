def recursion(n, v):
    if n == 3:
        print(v)
        return
    if M == 1:
        for i in range(1, 7):
            recursion(n + 1, v + str(i))
    elif M == 2:
        start = int(v[-1]) if v else 1
        for i in range(start, 7):
            recursion(n + 1, v + str(i))
    elif M == 3:
        for i in range(1, 7):
            if not str(i) in v:
                recursion(n + 1, v + str(i))


N, M = map(int, input().strip().split())
visited = [False] * 7
recursion(0, '')
