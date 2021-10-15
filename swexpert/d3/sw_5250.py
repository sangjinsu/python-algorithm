# 최소비용

# 좌 하 우 상
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    fuels[0][0] = 0
    queue = [(0, 0)]
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
    fuels = [[9999999999] * N for _ in range(N)]
    bfs()
    print('#{} {}'.format(t, fuels[N - 1][N - 1]))
