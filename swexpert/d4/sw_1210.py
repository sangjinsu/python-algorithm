test_cases = 10
# 하 좌 우
dx = [0, -1, 1]
dy = [1, 0, 0]
m = 100


def ladder(matrix, idx):
    direction = 0
    nx, ny = i, 0
    while ny < m - 1:
        tx, ty = nx + dx[direction], ny + dy[direction]
        if 0 <= tx < m and 0 <= ty < m:
            nx, ny = tx, ty
        if matrix[ny][nx] == 2:
            return idx
        direction = set_direction(direction, matrix, nx, ny)
    return -1


def set_direction(direction, matrix, nx, ny):
    if direction:
        if 0 <= ny + dy[0] < m:
            if matrix[ny + dy[0]][nx]:
                direction = 0
    else:
        # 좌우
        for d in range(1, 3):
            if 0 <= nx + dx[d] < m:
                if matrix[ny][nx + dx[d]]:
                    direction = d
    return direction


for t in range(1, test_cases + 1):
    case_num = int(input().strip())
    matrix = [list(map(int, input().strip().split())) for _ in range(m)]

    for i in range(m):
        if matrix[0][i]:
            found = ladder(matrix, i)
            if found != -1:
                print('#{} {}'.format(t, found))
                break
