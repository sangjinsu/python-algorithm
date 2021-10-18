def dfs(V):
    print(V, end=' ')
    visited[V] = True
    for n in graph[V]:
        if not visited[n]:
            dfs(n)


def dfs_s(V):
    stack = [V]
    visited[V] = True
    while stack:
        now = stack.pop()
        print(now, end=' ')
        for n in graph[now]:
            if not visited[n]:
                stack.append(n)
                visited[n] = True


def bfs(V):
    visited[V] = True
    queue = [V]
    while queue:
        now = queue.pop(0)
        print(now, end=' ')
        for n in graph[now]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True


N, M, V = map(int, input().strip().split())
visited = [False] * (N + 1)

graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

dfs(V)
visited = [False] * (N + 1)
print()
bfs(V)
