# 최소합
test_cases = int(input().strip())

dx = [1, 0]
dy = [0, 1]


def dfs(y, x, value):
    global result
    temp = mat[y][x]
    value += temp

    if y == N - 1 and x == N - 1:
        result = min(result, value)
        return
    if result < value:
        return

    mat[y][x] = -1
    for i in range(2):
        ty, tx = y + dy[i], x + dx[i]
        if 0 <= ty < N and 0 <= tx < N and mat[ty][tx] > 0:
            dfs(ty, tx, value)
    mat[y][x] = temp


for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [list(map(int, input().strip().split())) for _ in range(N)]
    result = 999999
    dfs(0, 0, 0)
    print('#{} {}'.format(t, result))
