import math


def prim():
    curV = 0
    D[curV] = 0

    while len(U) <= island:
        minV = math.inf
        for i in range(island):
            if i in U: continue
            if D[i] < minV:
                minV = D[i]
                curV = i
        U.append(curV)

        for i in range(island):
            if i in U: continue
            if 0 < graph[curV][i] < D[i]:
                D[i] = graph[curV][i]


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    island = int(input().strip())
    pos_x = list(map(int, input().strip().split()))
    pos_y = list(map(int, input().strip().split()))
    E = float(input().strip())

    graph = [[0] * island for _ in range(island)]

    for i in range(island):
        for j in range(i, island):
            weight = abs(pos_x[i] - pos_x[j]) ** 2 + abs(pos_y[i] - pos_y[j]) ** 2
            graph[i][j] = graph[j][i] = weight

    D = [math.inf] * island
    U = []
    prim()
    result = round(sum(D) * E)
    print('#{} {}'.format(t, result))