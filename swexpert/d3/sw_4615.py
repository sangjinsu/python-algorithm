dx = [0, 1, -1, 0, 1, -1, -1, 1]
dy = [1, 0, 0, -1, 1, 1, -1, -1]

test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())
    mat = [[0] * (N + 1) for _ in range(N + 1)]

    k = N // 2
    center = [
        (k, k, 2), (k, k + 1, 1),
        (k + 1, k, 1), (k + 1, k + 1, 2)
    ]
    for c in center:
        y, x, d = c
        mat[y][x] = d

    for _ in range(M):
        y, x, d = map(int, input().strip().split())
        mat[y][x] = d
        for i in range(8):
            ty, tx = y + dy[i], x + dx[i]
            queue = []
            while 0 < ty < N + 1 and 0 < tx < N + 1:
                if mat[ty][tx] == 0:
                    break
                if mat[ty][tx] == d:
                    for ty, tx in queue:
                        mat[ty][tx] = d
                    break
                queue.append((ty, tx))
                ty, tx = ty + dy[i], tx + dx[i]

    result = [0, 0, 0]
    for y in range(1, N + 1):
        for x in range(1, N + 1):
            result[mat[y][x]] += 1
    print('#{} {} {}'.format(t, result[1], result[2]))

