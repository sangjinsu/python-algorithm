import copy
from collections import deque

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(ny, nx):
    queue = deque()
    queue.append((ny, nx))
    temp_mat[ny][nx] = -1
    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < N and temp_mat[ty][tx] > 0:
                temp_mat[ty][tx] = -1
                queue.append((ty, tx))


N = int(input())
max_value = 0
mat = list()
for _ in range(N):
    row = list(map(int, input().split()))
    max_value = max(max_value, max(row))
    mat.append(row)

result = 0
for rain in range(max_value):
    temp_mat = copy.deepcopy(mat)
    for y in range(N):
        for x in range(N):
            if temp_mat[y][x] <= rain:
                temp_mat[y][x] = -1

    cnt = 0
    for y in range(N):
        for x in range(N):
            if temp_mat[y][x] > 0:
                bfs(y, x)
                cnt += 1
    result = max(result, cnt)

print(result)
