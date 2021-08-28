# 스택
test_cases = 10


def dfs(x, y):
    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    mat[y][x] = 1
    stack = [(x, y)]
    while stack:
        nx, ny = stack.pop()
        for i in range(4):
            tx, ty = nx + dx[i], ny + dy[i]
            if 0 <= tx < 16 and 0 <= ty < 16 and mat[ty][tx] != 1:
                if mat[ty][tx] == 3:
                    return 1
                mat[ty][tx] = 1
                stack.append((tx, ty))
    return 0


for t in range(1, test_cases + 1):
    test_num = int(input().strip())
    mat = [list(map(int, input().strip())) for _ in range(16)]

    for y in range(16):
        for x in range(16):
            if mat[y][x] == 2:
                result = dfs(x, y)
                print('#{} {}'.format(t, result))
                break
