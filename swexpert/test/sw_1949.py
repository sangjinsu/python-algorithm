# 우 하 좌 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def work(y, x, road, skill):
    global ans
    if road > ans:
        ans = road

    visited[y][x] = 1

    for i in range(4):
        ty, tx = y + dy[i], x + dx[i]
        if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx]:
            if mat[y][x] > mat[ty][tx]:
                work(ty, tx, road + 1, skill)

            elif skill and mat[y][x] > mat[ty][tx] - K:
                temp = mat[ty][tx]
                mat[ty][tx] = mat[y][x] - 1
                work(ty, tx, road + 1, 0)
                mat[ty][tx] = temp
    visited[y][x] = 0


# 2. 현재 위치를 들고 다닐 때
def work2(y, x, h, road, skill):
    global ans
    if road > ans:
        ans = road

    visited[y][x] = 1

    for i in range(4):
        ty, tx = y + dy[i], x + dx[i]
        if 0 <= ty < N and 0 <= tx < N and not visited[ty][tx]:
            if h > mat[ty][tx]:
                work2(ty, tx, mat[ty][tx], road + 1, skill)
            elif skill and h > mat[ty][tx] - K:
                work2(ty, tx, mat[y][x] - 1, road + 1, 0)

    visited[y][x] = 0


test_cases = int(input())
for t in range(1, test_cases + 1):
    N, K = map(int, input().split())

    mat = []
    max_h = 0
    for i in range(N):
        line = list(map(int, input().split()))
        mat.append(line)
        max_h = max(line + [max_h])

    visited = [[0] * N for _ in range(N)]
    ans = 0
    for y in range(N):
        for x in range(N):
            if mat[y][x] == max_h:
                # work(y, x, 1, 1)
                work2(y, x, max_h, 1, 1)

    print('#{} {}'.format(t, ans))
