def recursion(k):
    global cnt
    if k == N:
        cnt += 1
        if command == 1 and cnt == collect[0]:
            print(*t)
        if command == 2 and t == collect:
            print(cnt)

    else:
        for i in range(1, N + 1):
            if not visited[i]:
                t[k] = i
                visited[i] = True
                recursion(k + 1)
                visited[i] = False


N = int(input().strip())
command, *collect = map(int, input().strip().split())
visited = [False] * (N + 1)
t = [0] * N
cnt = 0
recursion(0)
