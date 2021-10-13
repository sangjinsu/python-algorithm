# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(ny, nx, value):
    if len(value) == 7:
        nums.add(value)
        return
    for i in range(4):
        ty, tx = ny + dy[i], nx + dx[i]
        if 0 <= ty < 4 and 0 <= tx < 4:
            dfs(ty, tx, value + mat[ty][tx])


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    mat = [input().strip().split() for _ in range(4)]
    nums = set()
    for y in range(4):
        for x in range(4):
            dfs(y, x, mat[y][x])
    print('#{} {}'.format(t, len(nums)))
