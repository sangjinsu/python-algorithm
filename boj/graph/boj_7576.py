import sys
from collections import deque
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(queue):
    for ny, nx in queue:
        mat[ny][nx] = 2

    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < M and mat[ty][tx] == 0:
                mat[ty][tx] = mat[ny][nx] + 1
                queue.append((ty, tx))


M, N = map(int, sys.stdin.readline().strip().split())
mat = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

queue = deque()
for y in range(N):
    for x in range(M):
        if mat[y][x] == 1:
            queue.append((y, x))

bfs(queue)
result = 0

for y in range(N):
    for x in range(M):
        if mat[y][x] == 0:
            result = -1
            break
        if mat[y][x] > result:
            result = mat[y][x]
    if result < 0:
        break
sys.stdout.write(str(-1) if result == -1 else str(result - 2))
