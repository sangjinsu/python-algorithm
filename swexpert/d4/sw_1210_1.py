test_cases = 10
# 상 좌 우
dx = [0, -1, 1]
dy = [-1, 0, 0]
m = 100


def ladder(matrix, i, m):
    direction = 0
    nx, ny = i, m - 1
    while ny != 0:
        tx, ty = nx + dx[direction], ny + dy[direction]
        if 0 <= tx < m and 0 <= ty < m:
            nx, ny = tx, ty
        direction = set_direction(direction, matrix, nx, ny)
    return nx


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


def search_endpoint(matrix):
    for i in range(m):
        if matrix[m - 1][i] == 2:
            return i


for t in range(1, test_cases + 1):
    case_num = int(input().strip())
    matrix = [list(map(int, input().strip().split())) for _ in range(m)]

    endpoint = search_endpoint(matrix)

    found = ladder(matrix, endpoint, m)
    print('#{} {}'.format(t, found))

