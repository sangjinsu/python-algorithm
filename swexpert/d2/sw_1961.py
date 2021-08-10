test_cases = int(input().strip())


def turn_matrix_90(matrix):
    matrix_90 = []
    for i in range(n):
        row = []
        for j in range(n - 1, -1, -1):
            row.append(matrix[j][i])
        matrix_90.append(row)
    return matrix_90


def turn_matrix_180(matrix):
    matrix_180 = []
    for i in range(n - 1, -1, -1):
        row = []
        for j in range(n - 1, -1, -1):
            row.append(matrix[i][j])
        matrix_180.append(row)
    return matrix_180


def turn_matrix_270(matrix):
    matrix_270 = []
    for i in range(n - 1, -1, -1):
        row = []
        for j in range(n):
            row.append(matrix[j][i])
        matrix_270.append(row)
    return matrix_270


for t in range(1, test_cases + 1):

    n = int(input().strip())

    matrix = []
    for i in range(n):
        row = input().strip().split()
        matrix.append(row)

    matrix_90 = turn_matrix_90(matrix)
    matrix_180 = turn_matrix_180(matrix)
    matrix_270 = turn_matrix_270(matrix)

    print(f'#{t}')
    for i in range(n):
        print(''.join(matrix_90[i]), ''.join(matrix_180[i]), ''.join(matrix_270[i]))
