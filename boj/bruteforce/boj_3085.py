import sys


def check():
    result = 0
    for i in range(0, n):
        row = 1
        col = 1
        for j in range(1, n):
            if mat[i][j] == mat[i][j - 1]:
                row += 1
            else:
                if row > result:
                    result = row
                row = 1

            if mat[j][i] == mat[j - 1][i]:
                col += 1
            else:
                if col > result:
                    result = col
                col = 1
        if row > result:
            result = row
        if col > result:
            result = col

    return result


n = int(sys.stdin.readline().strip())
mat = [list(sys.stdin.readline().strip()) for _ in range(n)]

result = 0
for y in range(n):
    for x in range(n - 1):
        mat[y][x], mat[y][x + 1] = mat[y][x + 1], mat[y][x]
        result = max(result, check())
        mat[y][x], mat[y][x + 1] = mat[y][x + 1], mat[y][x]

        mat[x][y], mat[x + 1][y] = mat[x + 1][y], mat[x][y]
        result = max(result, check())
        mat[x][y], mat[x + 1][y] = mat[x + 1][y], mat[x][y]

sys.stdout.write(str(result))
