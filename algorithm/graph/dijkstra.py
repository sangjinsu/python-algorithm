import heapq
import math

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n + 1)]
distance = [math.inf] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print(graph)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        print(q, distance)
        # start 지점 으로부터의 거리와 현재 위치
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == math.inf:
        print('cant')
    else:
        print(distance[i])
