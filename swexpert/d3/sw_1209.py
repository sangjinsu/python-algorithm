test_cases = 10

for t in range(1, test_cases + 1):
    case_num = int(input().strip())

    n = 100
    total_row, total_cols, total_r, total_le = 0, [0] * n, 0, 0

    for i in range(n):
        nums = list(map(int, input().strip().split()))
        total = 0
        for j in range(n):
            total += nums[j]
            total_cols[j] += nums[j]

            if i == j:
                total_r += nums[j]

            if n - i - 1 == j:
                total_le += nums[j]

        if total_row < total:
            total_row = total

    total_col = 0
    for col in total_cols:
        if total_col < col:
            total_col = col

    max_num = total_row
    for num in [total_col, total_r, total_le]:
        if max_num < num:
            max_num = num

    print('#{} {}'.format(case_num, max_num))
