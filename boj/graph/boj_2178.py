import sys
from collections import deque

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(y, x):
    mat[y][x] = 1
    queue = deque([(y, x)])
    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < M and mat[ty][tx] == '1':
                queue.append((ty, tx))
                mat[ty][tx] = mat[ny][nx] + 1


N, M = map(int, sys.stdin.readline().strip().split())
mat = [list(sys.stdin.readline().strip()) for _ in range(N)]
bfs(0, 0)
sys.stdout.write(str(mat[N - 1][M - 1]))
