from collections import deque

# 상 하 좌 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(mat):
    queue = deque()

    m = [[0] * M for _ in range(N)]

    for y in range(N):
        for x in range(M):
            m[y][x] = mat[y][x]
            if m[y][x] == 2:
                queue.append((y, x))

    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < M and m[ty][tx] == 0:
                m[ty][tx] = 2
                queue.append((ty, tx))
    cnt = 0
    for y in range(N):
        for x in range(M):
            if m[y][x] == 0:
                cnt += 1
    return cnt


def recursion(block):
    global result
    if block == 3:
        cnt = bfs(mat)
        result = max(cnt, result)
        return

    for y in range(N):
        for x in range(M):
            if mat[y][x] == 0:
                mat[y][x] = 1
                recursion(block + 1)
                mat[y][x] = 0


N, M = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

result = 0
recursion(0)
print(result)
