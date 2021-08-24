# 미로
test_cases = int(input().strip())


def find_route(nx, ny, mat, n, result):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    if mat[ny][nx] == 3:
        result[0] = 1
        return

    mat[ny][nx] = 1

    for i in range(4):
        tx, ty = nx + dx[i], ny + dy[i]
        if 0 <= tx < n and 0 <= ty < n and mat[ty][tx] != 1:
            find_route(tx, ty, mat, n, result)


def find_route_stack(nx, ny, mat, n):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    stack = []
    stack.append((nx, ny))

    mat[ny][nx] = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < n and 0 <= ty < n and mat[ty][tx] != 1:
                if mat[ty][tx] == 3:
                    return 1
                stack.append((tx, ty))
                mat[ty][tx] = 1

    return 0


for t in range(1, test_cases + 1):
    n = int(input().strip())
    mat = [list(map(int, input().strip())) for _ in range(n)]
    result = [0]
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 2:
                # find_route(j, i, mat, n, result)
                result = find_route_stack(j, i, mat, n)
    print('#{} {}'.format(t, result))
