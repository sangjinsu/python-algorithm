test_cases = int(input().strip())


def catch_flies(y, x, m, mat):
    total = 0
    for i in range(y, y + m):
        for j in range(x, x + m):
            total += mat[i][j]
    return total


for t in range(1, test_cases + 1):
    n, m = tuple(map(int, input().strip().split()))
    mat = [tuple(map(int, input().strip().split())) for _ in range(n)]

    flies = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            flies = max(flies, catch_flies(i, j, m, mat))

    print('#{} {}'.format(t, flies))
