# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

mat = [
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

queue = []
for y in range(4):
    for x in range(4):
        if mat[y][x] == 1:
            queue.append((y, x))

result = 0
while queue:
    ny, nx = queue.pop(0)
    for i in range(4):
        ty, tx = ny + dy[i], nx + dx[i]
        if 0 <= ty < 4 and 0 <= tx < 4 and mat[ty][tx] == 0:
            mat[ty][tx] = mat[ny][nx] + 1
            queue.append((ty, tx))
            result = max(result, mat[ty][tx])
print(mat)
print(result)
