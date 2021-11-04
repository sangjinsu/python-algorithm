from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solve():
    for y in range(100):
        for x in range(100):
            if mat[y][x] == '2':
                return bfs(y, x)


def bfs(y, x):
    Q = deque([(y, x)])
    while Q:
        ny, nx = Q.popleft()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < 100 and 0 <= tx < 100 and mat[ty][tx] in ['0', '3']:
                if mat[ty][tx] == '3':
                    return 1
                Q.append((ty, tx))
                mat[ty][tx] = '5'
    return 0


test_cases = 10
for t in range(1, test_cases + 1):
    T = int(input().strip())
    mat = [list(input().strip()) for _ in range(100)]
    result = solve()
    print('#{} {}'.format(t, result))
