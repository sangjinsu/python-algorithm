# 최소 이동 거리
import math


def dijkstra():
    curV = 0
    visited = [curV]
    for w, v in graph[curV]:
        if w > 0:
            dist[v][curV] = w

    while len(visited) <= N:
        minV = math.inf
        for i in range(N + 1):
            if i in visited: continue
            if dist[i][0] < minV:
                minV = dist[i][0]
                curV = i

        visited.append(curV)
        for w, v in graph[curV]:
            if v in visited:
                continue
            if w > 0:
                if dist[v][0] > dist[curV][0] + w:
                    dist[v][0] = dist[curV][0] + w
                    dist[v][1] = curV


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    dist = [[math.inf, 0] for _ in range(N + 1)]
    for i in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
    dijkstra()
    print('#{} {}'.format(t, dist[-1][0]))
