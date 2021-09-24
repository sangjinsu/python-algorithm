import sys

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(y, x):
    cnt = 1
    mat[y][x] = -1
    stack = [(y, x)]
    while stack:
        ny, nx = stack.pop()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= tx < n and 0 <= ty < n and mat[ty][tx] == 1:
                stack.append((ty, tx))
                mat[ty][tx] = -1
                cnt += 1
    return cnt


n = int(sys.stdin.readline())
mat = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]

result = []
for y in range(n):
    for x in range(n):
        if mat[y][x] == 1:
            result.append(dfs(y, x))

result.sort()
sys.stdout.write(str(len(result)) + '\n')
for i in result:
    sys.stdout.write(str(i) + '\n')
