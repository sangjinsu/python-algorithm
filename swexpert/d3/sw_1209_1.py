test_cases = 10

for t in range(1, test_cases + 1):
    case_num = int(input().strip())

    n = 100
    matrix = []

    total_row, total_col, total_r, total_le = 0, 0, 0, 0

    for i in range(n):
        row = list(map(int, input().strip().split()))
        matrix.append(row)

    for i in range(n):
        row_sum = 0
        col_sum = 0
        for j in range(n):
            row_sum += matrix[i][j]
            col_sum += matrix[j][i]

            if i == j:
                total_r += matrix[i][j]

            if n - i - 1 == j:
                total_le += matrix[i][j]

        if total_row < row_sum:
            total_row = row_sum

        if total_col < col_sum:
            total_col = col_sum

    max_num = total_row
    for num in [total_col, total_r, total_le]:
        if max_num < num:
            max_num = num

    print('#{} {}'.format(case_num, max_num))