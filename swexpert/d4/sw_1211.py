from collections import deque

# 우 좌 하
dx = [1, -1, 0]
dy = [0, 0, 1]


def bfs(y, x):
    Q = deque([(y, x, 0)])
    visited[y][x] = True
    while Q:
        ny, nx, k = Q.popleft()
        if ny == 99:
            return k
        for i in range(3):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < 100 and 0 <= tx < 100 and mat[ty][tx] == '1' and not visited[ty][tx]:
                visited[ty][tx] = True
                Q.append((ty, tx, k + 1))
                break


testCases = 10
for t in range(1, testCases + 1):
    N = int(input())
    mat = [input().strip().split() for _ in range(100)]
    check_cnt = min_cnt = 999999

    result = 0
    for x in range(100):
        if mat[0][x] == '1':
            visited = [[False] * 100 for _ in range(100)]
            min_cnt = bfs(0, x)
            if min_cnt < check_cnt:
                check_cnt = min_cnt
                result = x

    print('#{} {}'.format(t, result))
