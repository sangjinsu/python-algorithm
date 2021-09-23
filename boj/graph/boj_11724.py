import sys
sys.setrecursionlimit(10000)

def dfs(k):
    visited[k] = True
    for v in graph[k]:
        if not visited[v]:
            dfs(v)


N, M = map(int, sys.stdin.readline().strip().split())

visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        cnt += 1
        dfs(i)

sys.stdout.write(str(cnt))