# 미로의 거리
test_cases = int(input().strip())


def bfs(x, y):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    mat[y][x] = -1
    queue = [(x, y)]

    while queue:
        nx, ny = queue.pop(0)
        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]
            if 0 <= tx < n and 0 <= ty < n and (mat[ty][tx] == 0 or mat[ty][tx] == 3):
                if mat[ty][tx] == 3:
                    return -mat[ny][nx] - 1
                queue.append((tx, ty))
                mat[ty][tx] = mat[ny][nx] - 1
    return 0


for t in range(1, test_cases + 1):
    n = int(input().strip())
    mat = [list(map(int, input().strip())) for _ in range(n)]

    result = 0
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 2:
                result = bfs(j, i)
                break

    print('#{} {}'.format(t, result))
