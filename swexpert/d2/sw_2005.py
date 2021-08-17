test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n = int(input().strip())
    mat = [[0] * i for i in range(1, n + 1)]

    for i in range(n):
        mat[i][0], mat[i][-1] = 1, 1
        for j in range(1, i):
            mat[i][j] = mat[i - 1][j - 1] + mat[i - 1][j]

    print(f'#{t}')
    for row in mat:
        print(' '.join(map(str, row)))
    print('ABCDE'[4:3])