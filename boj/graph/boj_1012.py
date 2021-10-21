import sys

sys.setrecursionlimit(10000)
# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(y, x):
    mat[y][x] = 2
    for i in range(4):
        ty, tx = y + dy[i], x + dx[i]
        if 0 <= ty < N and 0 <= tx < M and mat[ty][tx] == 1:
            dfs(ty, tx)


test_cases = int(input())
for t in range(test_cases):
    M, N, K = map(int, input().strip().split())
    mat = [[0] * M for _ in range(N)]

    for _ in range(K):
        a, b = map(int, input().strip().split())
        mat[b][a] = 1

    result = 0
    for y in range(N):
        for x in range(M):
            if mat[y][x] == 1:
                dfs(y, x)
                result += 1
    print(result)
