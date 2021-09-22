import sys


def dfs(k, cnt):
    global result
    if cnt == 4:
        result = 1
        return

    visited[k] = True
    for v in graph[k]:
        if not visited[v]:
            dfs(v, cnt + 1)
        if result:
            return
    visited[k] = False


n, m = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
for i in range(n):

    dfs(i, 0)

sys.stdout.write(str(result))
