import sys
sys.setrecursionlimit(100000)

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(ny, nx, color):
    for i in range(4):
        ty, tx = ny + dy[i], nx + dx[i]
        if 0 <= ty < N and 0 <= tx < N and mat[ty][tx] in color and not visited[ty][tx]:
            visited[ty][tx] = True
            dfs(ty, tx, color)


N = int(input().strip())

mat = [input().strip() for _ in range(N)]
visited = [[False] * N for _ in range(N)]

cnt = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            cnt += 1
            dfs(y, x, mat[y][x])

print(cnt)

visited = [[False] * N for _ in range(N)]
cnt = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            cnt += 1
            if mat[y][x] in 'RG':
                dfs(y, x, 'RG')
            else:
                dfs(y, x, mat[y][x])

print(cnt)
