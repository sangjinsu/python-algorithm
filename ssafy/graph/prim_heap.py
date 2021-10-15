import heapq


def Prim():
    visited = [0] * (V + 1)
    heap = []
    heapq.heappush(heap, (0, 0))
    result = 0
    while heap:
        w, v = heapq.heappop(heap)
        if not visited[v]:
            result += w
            visited[v] = 1
            for idx, weight in adj[v]:
                if not visited[idx]:
                    heapq.heappush(heap, (weight, idx))
    return result


test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    V, E = map(int, input().strip().split())
    adj = [[] for _ in range(V + 1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        adj[n1].append((n2, w))
        adj[n2].append((n1, w))
