# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs(y, x):
    queue = [(y, x)]
    visited[y][x] = True
    cnt = 1
    while queue:
        ny, nx = queue.pop(0)
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx] and mat[ty][tx] == '1':
                visited[ty][tx] = True
                queue.append((ty, tx))
                cnt += 1
    return cnt


N = int(input())
mat = [input() for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dangi = []
for y in range(N):
    for x in range(N):
        if not visited[y][x] and mat[y][x] == '1':
            dangi.append(bfs(y, x))

dangi.sort()
print(len(dangi))
for i in dangi:
    print(i)
