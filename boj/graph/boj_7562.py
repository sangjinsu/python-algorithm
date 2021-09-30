import sys

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]


def bfs(y, x):
    mat[y][x] = 0
    if y == ay and x == ax:
        return
    queue = [(y, x)]
    while queue:
        ny, nx = queue.pop(0)
        for i in range(8):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= tx < I and 0 <= ty < I and mat[ty][tx] == -1:
                mat[ty][tx] = mat[ny][nx] + 1
                if ty == ay and tx == ax:
                    return
                queue.append((ty, tx))


test_cases = int(sys.stdin.readline().strip())
for t in range(1, test_cases + 1):
    I = int(sys.stdin.readline().strip())

    x, y = map(int, sys.stdin.readline().strip().split())
    ax, ay = map(int, sys.stdin.readline().strip().split())

    mat = [[-1] * I for _ in range(I)]
    bfs(y, x)
    sys.stdout.write(str(mat[ay][ax]) + '\n')
