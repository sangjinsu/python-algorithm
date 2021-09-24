# from collections import deque

test_cases = int(input())

# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(queue, front, rear):
    result = 0
    # queue = deque(queue)
    # while queue:
    while front != rear:
        # ny, nx = queue.popleft()
        front += 1
        ny, nx = queue[front]
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < M and mat[ty][tx] == 'L' and not visited[ty][tx]:
                # queue.append((ty, tx))
                rear += 1
                queue[rear] = (ty, tx)
                visited[ty][tx] = visited[ny][nx] + 1
                result += visited[ty][tx]
    return result


for t in range(1, test_cases + 1):
    N, M = map(int, input().split())
    mat = [input() for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    queue = [0] * N * M
    front = -1
    rear = -1

    for y in range(N):
        for x in range(M):
            if mat[y][x] == 'W':
                # queue.append((y, x))
                rear += 1
                queue[rear] = (y, x)

    result = bfs(queue, front, rear)

    print('#{} {}'.format(t, result))
