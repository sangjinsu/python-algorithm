import math


def dijkstra(start, G, D):
    D[start] = 0
    curV = start
    U = [curV]
    for i in range(N + 1):
        if G[curV][i] > 0:
            D[i] = G[curV][i]

    while len(U) <= N:
        minV = math.inf
        for i in range(N + 1):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                curV = i

        U.append(curV)
        for i in range(N + 1):
            if i in U: continue
            if G[curV][i] > 0:
                if D[i] > D[curV] + G[curV][i]:
                    D[i] = D[curV] + G[curV][i]


test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N, M, X = map(int, input().strip().split())
    graph1 = [[0] * (N + 1) for _ in range(N + 1)]
    graph2 = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        x, y, c = map(int, input().strip().split())
        graph1[x][y] = c
        graph2[y][x] = c

    distance1 = [math.inf] * (N + 1)
    distance2 = [math.inf] * (N + 1)
    dijkstra(X, graph1, distance1)
    dijkstra(X, graph2, distance2)

    result = 0
    for i in range(1, N + 1):
        result = max(result, distance1[i] + distance2[i])
    print('#{} {}'.format(t, result))
