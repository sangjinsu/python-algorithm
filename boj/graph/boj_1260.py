import sys


def dfs(k):
    visited[k] = True
    sys.stdout.write(str(k) + ' ')
    for v in graph[k]:
        if not visited[v]:
            dfs(v)


def bfs(k):
    visited = [False] * (N + 1)
    visited[k] = True
    queue = [k]
    while queue:
        node = queue.pop(0)
        sys.stdout.write(str(node) + ' ')
        for n in graph[node]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True


N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
dfs(V)
print()

bfs(V)
