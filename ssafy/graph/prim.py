"""
6 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
"""
import math


def prim():
    curV = 0
    D[curV][0] = 0

    while len(U) <= N:
        # D의 key 값이 최소인 정점을 구한다
        # 이 정점은 U에 포함되지 않아야 한다
        minV = math.inf
        for i in range(N + 1):
            if i in U: continue
            if D[i][0] < minV:
                minV = D[i][0]
                curV = i
        # U에 추가
        U.append(curV)

        # curV 의 인접한 정점의 가중치를 사용하면 D를 업데이트
        for i in range(N + 1):
            if i in U: continue
            if 0 < G[curV][i] < D[i][0]:
                D[i][0] = G[curV][i]
                D[i][1] = curV


N, E = map(int, input().split())
G = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(E):
    s1, s2, w = map(int, input().split())
    G[s1][s2] = w
    G[s2][s1] = w

D = [[math.inf, 0] for _ in range(N + 1)]
U = []

prim()
print(D)
print(U)
