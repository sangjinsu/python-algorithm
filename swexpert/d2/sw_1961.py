test_cases = int(input().strip())


# def turn_matrix_90(matrix, n):
#     matrix_90 = []
#     for i in range(n):
#         row = []
#         for j in range(n - 1, -1, -1):
#             row.append(matrix[j][i])
#         matrix_90.append(row)
#     return matrix_90

def turn_matrix_90(matrix, n):
    matrix_90 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_90[j][n - i - 1] = matrix[i][j]
    return matrix_90


# def turn_matrix_180(matrix):
#     matrix_180 = []
#     for i in range(n - 1, -1, -1):
#         row = []
#         for j in range(n - 1, -1, -1):
#             row.append(matrix[i][j])
#         matrix_180.append(row)
#     return matrix_180


def turn_matrix_180(matrix, n):
    matrix_180 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_180[n - i - 1][n - j - 1] = matrix[i][j]
    return matrix_180


# def turn_matrix_270(matrix, n):
#     matrix_270 = []
#     for i in range(n - 1, -1, -1):
#         row = []
#         for j in range(n):
#             row.append(matrix[j][i])
#         matrix_270.append(row)
#     return matrix_270

def turn_matrix_270(matrix, n):
    matrix_270 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_270[n - j - 1][i] = matrix[i][j]
    return matrix_270


for t in range(1, test_cases + 1):

    n = int(input().strip())

    matrix = [input().strip().split() for _ in range(n)]

    matrix_90 = turn_matrix_90(matrix, n)
    matrix_180 = turn_matrix_90(matrix_90, n)
    matrix_270 = turn_matrix_90(matrix_180, n)

    print(f'#{t}')
    for i in range(n):
        print(''.join(matrix_90[i]), ''.join(matrix_180[i]), ''.join(matrix_270[i]))
