test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())
    mat = [input().strip() for _ in range(N)]
    division = []
    for i in range(1, N):
        for j in range(1, N - i):
            k = N - i - j
            division.append((i, j, k))

    result = 999999

    for W, B, R in division:
        cnt = 0
        for y in range(W):
            for x in range(M):
                if mat[y][x] == 'W':
                    cnt += 1
        if cnt > result:
            continue
        for y in range(W, W + B):
            for x in range(M):
                if mat[y][x] == 'B':
                    cnt += 1
        if cnt > result:
            continue
        for y in range(W + B, W + B + R):
            for x in range(M):
                if mat[y][x] == 'R':
                    cnt += 1
        if cnt > result:
            continue
        result = min(result, M * N - cnt)

    print('#{} {}'.format(t, result))
