"""
5 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
"""
import math


def dijkstra():
    curV = 0
    U = [curV]
    for i in range(N + 1):
        if G[curV][i] > 0:
            D[i][curV] = G[curV][i]

    while len(U) <= N:
        minV = math.inf
        for i in range(N + 1):
            if i in U: continue
            if D[i][0] < minV:
                minV = D[i][0]
                curV = i

        U.append(curV)
        for i in range(N + 1):
            if i in U: continue
            if G[curV][i] > 0:
                if D[i][0] > D[curV][0] + G[curV][i]:
                    D[i][0] = D[curV][0] + G[curV][i]
                    D[i][1] = curV


N, E = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
D = [[math.inf, 0] for _ in range(N + 1)]
for i in range(E):
    s1, s2, w = map(int, input().split())
    G[s1][s2] = w

dijkstra()
print(D)

