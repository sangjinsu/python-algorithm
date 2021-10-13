def dfs(start, cnt):
    global max_cnt
    visited[start] = True
    if cnt > max_cnt:
        max_cnt = cnt

    for node in graph[start]:
        if not visited[node]:
            dfs(node, cnt + 1)

    visited[start] = False


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        x, y = map(int, input().strip().split())
        graph[x].append(y)
        graph[y].append(x)

    visited = [False] * (N + 1)

    max_cnt = 0
    for i in range(1, N + 1):
        dfs(i, 1)

    print('#{} {}'.format(t, max_cnt))
