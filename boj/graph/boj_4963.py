import sys
sys.setrecursionlimit(10000)
# 상 우 하 좌 + 상우 하우 좌하 좌상
dx = [0, 1, 0, -1] + [1, 1, -1, -1]
dy = [-1, 0, 1, 0] + [-1, 1, 1, -1]


def dfs(y, x):
    mat[y][x] = 2
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < h and 0 <= nx < w and mat[ny][nx] == 1:
            dfs(ny, nx)


while True:
    w, h = map(int, sys.stdin.readline().strip().split())

    if w == 0 and h == 0:
        break

    mat = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]
    cnt = 0

    for y in range(h):
        for x in range(w):
            if mat[y][x] == 1:
                cnt += 1
                dfs(y, x)

    sys.stdout.write(str(cnt) + '\n')
