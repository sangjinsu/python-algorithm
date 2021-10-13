dy = [1, 1, -1, -1]
dx = [-1, 1, 1, -1]


def recursion(sy, sx, ny, nx, d, k):
    global result

    if d == 4:
        return

    if sy == ny and sx == nx and d == 3:
        result = max(result, k)
        return

    if 0 <= ny < N and 0 <= nx < N and not nums[mat[ny][nx]]:
        nums[mat[ny][nx]] = True
        recursion(sy, sx, ny + dy[d], nx + dx[d], d, k + 1)
        recursion(sy, sx, ny + dy[(d + 1) % 4], nx + dx[(d + 1) % 4], d + 1, k + 1)
        nums[mat[ny][nx]] = False


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [list(map(int, input().strip().split())) for _ in range(N)]
    nums = [False] * 101
    result = -1
    for y in range(N):
        for x in range(N):
            if not (y, x) in [(0, 0), (N - 1, N - 1), (0, N - 1), (N - 1, 0)]:
                recursion(y, x, y, x, 0, 0)

    print('#{} {}'.format(t, result))
