import sys


def rotate():
    check = min(N, M) // 2

    for i in range(check):
        n_max = N - i - 1
        m_max = M - i - 1

        temp = mat[i][i]

        for j in range(i, m_max):
            mat[i][j] = mat[i][j + 1]

        for j in range(i, n_max):
            mat[j][m_max] = mat[j + 1][m_max]

        for j in range(m_max, i, -1):
            mat[n_max][j] = mat[n_max][j - 1]

        for j in range(n_max, i, -1):
            mat[j][i] = mat[j - 1][i]

        mat[i + 1][i] = temp


N, M, R = map(int, sys.stdin.readline().split())

mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for _ in range(R):
    rotate()

for i in range(N):
    for j in range(M):
        sys.stdout.write(str(mat[i][j]) + ' ')
    print()
