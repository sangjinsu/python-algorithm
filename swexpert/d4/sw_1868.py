from collections import deque

# 상 하 좌 우 + 우상 우하 좌상 좌하
dx = [0, 0, -1, 1] + [1, 1, -1, -1]
dy = [-1, 1, 0, 0] + [-1, 1, -1, 1]

test_cases = int(input().strip())


def hasStar(y, x):
    for i in range(8):
        ty, tx = y + dy[i], x + dx[i]
        if 0 <= ty < N and 0 <= tx < N:
            if mat[ty][tx] == '*':
                return True
    return False


def bfs(y, x):
    Q.append((y, x))
    visited[y][x] = True
    while Q:
        ny, nx = Q.popleft()
        for i in range(8):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx]:
                visited[ty][tx] = True
                if not hasStar(ty, tx):
                    Q.append((ty, tx))


for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [input().strip() for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    Q = deque()
    result = 0
    for y in range(N):
        for x in range(N):
            if mat[y][x] == '.' and not hasStar(y, x) and not visited[y][x]:
                bfs(y, x)
                result += 1

    for y in range(N):
        for x in range(N):
            if mat[y][x] == '.' and not visited[y][x]:
                result += 1

    print('#{} {}'.format(t, result))
