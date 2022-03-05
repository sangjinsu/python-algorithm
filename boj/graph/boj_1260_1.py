from collections import deque


def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for adj in graph[v]:
        if not visited[adj]:
            visited[adj] = True
            dfs(adj)


def bfs(v):
    visited = [False] * (N + 1)
    queue = deque([v])
    visited[v] = True
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        for adj in graph[vertex]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True


N, M, V = map(int, input().strip().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    s, e = map(int, input().strip().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
dfs(V)
print()

bfs(V)
