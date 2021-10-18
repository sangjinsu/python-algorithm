from pprint import pprint

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(y, x):
    global result
    queue = [(y, x)]
    mat[y][x] = 1
    while queue:
        ny, nx = queue.pop(0)
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < 3 and 0 <= tx < 4 and mat[ty][tx] == 0:
                mat[ty][tx] = mat[ny][nx] + 1
                result = max(result, mat[ty][tx])
                queue.append((ty, tx))


mat = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

result = 0
bfs(1, 1)
print(mat)
print(result)
