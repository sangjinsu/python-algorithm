dx = [-1, 1, -2, 2, -1, 1]
dy = [-2, -2, 0, 0, 2, 2]

N = int(input())

sy, sx, ey, ex = map(int, input().split())

queue = [(sy, sx, 0)]
visited = [[False] * N for _ in range(N)]
result = -1
while queue:
    ny, nx, cnt = queue.pop(0)

    if ny == ey and nx == ex:
        result = cnt
        break

    for i in range(6):
        ty, tx = ny + dy[i], nx + dx[i]

        if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx]:
            visited[ty][tx] = True
            queue.append((ty, tx, cnt + 1))
print(result)
