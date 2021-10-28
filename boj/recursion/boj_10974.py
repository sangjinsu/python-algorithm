def recursion(k):
    if k == N:
        print(*result)

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            recursion(k + 1)
            visited[i] = False
            result.pop()


N = int(input())
visited = [False] * (N + 1)
result = []
recursion(0)
