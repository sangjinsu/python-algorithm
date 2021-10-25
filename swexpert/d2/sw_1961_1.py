def turn_90(mat):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][N - i - 1] = mat[i][j]
    return temp


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    mat = [input().strip().split() for _ in range(N)]
    mat_90 = turn_90(mat)
    mat_180 = turn_90(mat_90)
    mat_270 = turn_90(mat_180)

    print('#{}'.format(t))
    for i in range(N):
        for m in [mat_90, mat_180, mat_270]:
            print(''.join(m[i]), end=' ')
        print()
