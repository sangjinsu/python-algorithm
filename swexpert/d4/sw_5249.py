# 최소 신장 트리
import math


def prim():
    curV = 0
    dist[curV][0] = 0

    while len(visited) <= V:
        minV = math.inf
        for i in range(V + 1):
            if i in visited: continue
            if dist[i][0] < minV:
                minV = dist[i][0]
                curV = i
        visited.append(curV)
        for w, v in graph[curV]:
            if v in visited:
                continue
            if 0 < w < dist[v][0]:
                dist[v][0] = w
                dist[v][1] = v


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    V, E = map(int, input().strip().split())
    graph = [[] for _ in range(V + 1)]
    for i in range(E):
        u, v, w = map(int, input().strip().split())
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = []
    dist = [[math.inf, 0] for _ in range(V + 1)]
    prim()
    result = 0
    for d in dist:
        result += d[0]

    print('#{} {}'.format(t, result))
