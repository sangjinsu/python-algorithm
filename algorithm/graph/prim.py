import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    u, v, weight = map(int, input().split())
    graph[u].append((weight, u, v))
    graph[v].append((weight, v, u))


def prim(start):
    visited[start] = True
    candidate = graph[start]
    heapq.heapify(candidate)
    mst = []
    result = 0

    while candidate:
        weight, u, v = heapq.heappop(candidate)
        if not visited[v]:
            visited[v] = True
            mst.append((u, v))
            result += weight

            for edge in graph[v]:
                if not visited[edge[2]]:
                    heapq.heappush(candidate, edge)
    return result, mst


print(prim(1))
