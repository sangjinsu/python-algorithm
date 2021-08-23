test_cases = 10

for t in range(1, test_cases + 1):
    test_num = int(input())
    mat = [list(map(int, input().strip().split())) for _ in range(100)]

    tot_row = 0
    tot_col = 0
    tot_left_cross = 0
    tot_right_cross = 0
    for i in range(100):
        row = 0
        col = 0
        for j in range(100):
            row += mat[i][j]
            col += mat[j][i]

            if i == j:
                tot_left_cross += mat[i][j]

            if 99 - i == j:
                tot_right_cross += mat[i][j]

        if tot_row < row:
            tot_row = row
        if tot_col < col:
            tot_col = col

    m = tot_col
    for n in [tot_row, tot_right_cross, tot_left_cross]:
        if m < n:
            m = n

    print('#{} {}'.format(t, m))
