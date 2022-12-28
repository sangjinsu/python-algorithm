import sys


def dfs(v: int, depth: int):
    global existed
    if depth == 4 or existed == 1:
        existed = 1
        return

    visited[v] = True
    for u in graph[v]:
        if not visited[u]:
            dfs(u, depth + 1)
    visited[v] = False


N, M = map(int, sys.stdin.readline().strip().split())

graph: list[list[int]] = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

existed = 0
visited = [False] * N
for i in range(N):
    dfs(i, 0)

sys.stdout.write(str(existed))
