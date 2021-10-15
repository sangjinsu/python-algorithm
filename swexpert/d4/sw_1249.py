# 보급로
import heapq

# 좌 하 우 상
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs():
    time[0][0] = 0
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    while queue:
        dist, ny, nx = heapq.heappop(queue)
        for i in range(4):
            ty, tx = ny + dy[i], nx + dx[i]
            if 0 <= ty < N and 0 <= tx < N:
                if time[ty][tx] > time[ny][nx] + mat[ty][tx]:
                    time[ty][tx] = time[ny][nx] + mat[ty][tx]
                    heapq.heappush(queue, (time[ty][tx], ty, tx))


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [list(map(int, list(input().strip()))) for _ in range(N)]
    time = [[9999999999] * N for _ in range(N)]
    bfs()

    print('#{} {}'.format(t, time[N - 1][N - 1]))
