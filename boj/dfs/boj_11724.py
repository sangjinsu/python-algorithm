import sys

sys.setrecursionlimit(10000)


def dfs(v: int):
    visited[v] = True
    for node in graph[v]:
        if not visited[node]:
            dfs(node)


N, M = map(int, sys.stdin.readline().strip().split())

graph: list[list[int]] = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
result = 0
for v in range(1, N + 1):
    if not visited[v]:
        dfs(v)
        result += 1

sys.stdout.write(str(result))
