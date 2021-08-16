test_cases = int(input().strip())
m = 9


def check_square(matrix, i, j):
    checkerboard = []
    for k in range(i, i + 3):
        for l in range(j, j + 3):
            if matrix[k][l] in checkerboard:
                return False
            else:
                checkerboard.append(matrix[k][l])
    return True


def check_row_column(matrix, i):
    row_checkerboard = []
    col_checkerboard = []
    for j in range(m):
        if matrix[i][j] in row_checkerboard:
            return False
        else:
            row_checkerboard.append(matrix[i][j])

        if matrix[j][i] in col_checkerboard:
            return False
        else:
            col_checkerboard.append(matrix[j][i])

    return True


def solution(tc):
    matrix = [list(input().strip().split()) for _ in range(m)]

    for i in range(0, m, 3):
        for j in range(0, m, 3):
            result = check_square(matrix, i, j)
            if not result:
                print('#{} {}'.format(tc, 0))
                return

    for i in range(m):
        result = check_row_column(matrix, i)
        if not result:
            print('#{} {}'.format(tc, 0))
            return

    print('#{} {}'.format(tc, 1))


for t in range(1, test_cases + 1):
    solution(t)
