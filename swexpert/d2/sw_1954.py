test_cases = int(input())

# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for t in range(1, test_cases + 1):
    n = int(input())
    matrix = [[0] * n for _ in range(n)]

    mark = 0
    nx, ny = 0, 0
    direction = 0
    for i in range(n * n):
        mark += 1
        if not matrix[ny][nx]:
            matrix[ny][nx] = mark

        tx, ty = nx + dx[direction], ny + dy[direction]
        if tx < 0 or tx >= n or ty < 0 or ty >= n:
            direction = (direction + 1) % 4
        elif matrix[ty][tx]:
            direction = (direction + 1) % 4

        nx, ny = nx + dx[direction], ny + dy[direction]

    print('#{}'.format(t))
    for row in matrix:
        print(*row)
