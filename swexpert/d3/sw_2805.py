test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [list(map(int, list(input().strip()))) for _ in range(N)]
    result = 0

    s, e = N // 2, N // 2
    for i in range(N):
        if i < N // 2:
            for j in range(s, e + 1):
                result += mat[i][j]
            s -= 1
            e += 1
        elif i == N // 2:
            for j in range(s, e + 1):
                result += mat[i][j]
        elif i > N // 2:
            s += 1
            e -= 1
            for j in range(s, e + 1):
                result += mat[i][j]

    print('#{} {}'.format(t, result))
