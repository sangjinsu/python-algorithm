import sys
from collections import deque

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(mat, visited, y, x):
    visited[y][x] = 1
    q = deque([(y, x)])

    while q:
        ny, nx = q.popleft()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= tx < M and 0 <= ty < N and mat[ty][tx] == 1 and not visited[ty][tx]:
                visited[ty][tx] = visited[ny][nx] + 1
                q.append((ty, tx))


if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    mat = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    bfs(mat, visited, 0, 0)

    sys.stdout.write(str(visited[N - 1][M - 1]))
