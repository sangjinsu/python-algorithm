# 재귀
test_cases = 10

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(nx, ny, result):
    if mat[ny][nx] == 3:
        result[0] = 1
        return

    mat[ny][nx] = 1
    for i in range(4):
        tx, ty = nx + dx[i], ny + dy[i]
        if 0 <= tx < 16 and 0 <= ty < 16 and mat[ty][tx] != 1:
            dfs(tx, ty, result)


for t in range(1, test_cases + 1):
    test_num = int(input().strip())
    mat = [list(map(int, input().strip())) for _ in range(16)]
    result = [0]
    for y in range(16):
        for x in range(16):
            if mat[y][x] == 2:
                dfs(x, y, result)
                break
    print('#{} {}'.format(t, result[0]))
