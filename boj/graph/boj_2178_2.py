from collections import deque

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs():
    queue = deque([(0, 0)])
    visited[0][0] = 1
    while queue:
        ny, nx = queue.popleft()
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < M and mat[ty][tx] == '1':
                if visited[ny][nx] + 1 < visited[ty][tx]:
                    visited[ty][tx] = visited[ny][nx] + 1
                    queue.append((ty, tx))


N, M = map(int, input().strip().split())

mat = [input() for _ in range(N)]
visited = [[10 ** 5] * M for _ in range(N)]
bfs()
print(visited[-1][-1])
