test_cases = int(input().strip())


def get_days_of_month(month):
    if month == 2:
        return 28
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    return 30


for i in range(1, test_cases + 1):
    month1, day1, month2, day2 = map(int, input().strip().split())

    if month1 == month2:
        print('#{} {}'.format(i, day2 - day1 + 1))
    else:
        total = 0
        for j in range(month1, month2):
            total += get_days_of_month(j)

        total = total - day1 + 1
        total += day2
        print('#{} {}'.format(i, total))
