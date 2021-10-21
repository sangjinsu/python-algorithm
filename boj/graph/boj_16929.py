import sys

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(ny, nx, color, py, px):
    if visited[ny][nx]:
        return True
    visited[ny][nx] = True
    for i in range(4):
        ty, tx = ny + dy[i], nx + dx[i]
        if 0 <= ty < N and 0 <= tx < M:
            if ty != py or tx != px:
                if mat[ty][tx] == color:
                    if dfs(ty, tx, color, ny, nx):
                        return True

    return False


N, M = map(int, sys.stdin.readline().split())
mat = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = False
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            result = dfs(i, j, mat[i][j], 0, 0)
            if result:
                sys.stdout.write('Yes')
                break
    if result:
        break
if not result:
    sys.stdout.write('No')
