import math

# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(y, x):
    fuels[y][x] = mat[y][x]
    queue = [(y, x)]
    while queue:
        ny, nx = queue.pop(0)
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < N:
                fuel = 1
                if mat[ty][tx] > mat[ny][nx]:
                    fuel += mat[ty][tx] - mat[ny][nx]
                if fuels[ty][tx] > fuels[ny][nx] + fuel:
                    fuels[ty][tx] = fuels[ny][nx] + fuel
                    queue.append((ty, tx))


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [list(map(int, input().strip().split())) for _ in range(N)]
    fuels = [[math.inf] * N for _ in range(N)]
    bfs(0, 0)
    result = fuels[N - 1][N - 1]
    print('#{} {}'.format(t, result))
