import heapq
import math

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [math.inf] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[0]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
