dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

mat = [
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

queue = []
queue.append((0, 0))

mat[0][0] = -1
while queue:
    ny, nx = queue.pop(0)
    if ny == 3 and nx == 4: break
    for i in range(4):
        ty, tx = ny + dy[i], nx + dx[i]
        if 0 <= ty < 4 and 0 <= tx < 5 and mat[ty][tx] == 0:
            queue.append((ty, tx))
            mat[ty][tx] = mat[ny][nx] - 1
print(-mat[3][4])
