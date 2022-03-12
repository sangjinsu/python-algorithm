import heapq
import math

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [math.inf] * (N + 1)


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (start, 0))
    distance[start] = 0

    while queue:
        now, dist = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for adj in graph[now]:
            cost = adj[1] + dist
            if cost < distance[adj[0]]:
                distance[adj[0]] = cost
                heapq.heappush(queue, (adj[0], cost))


start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
