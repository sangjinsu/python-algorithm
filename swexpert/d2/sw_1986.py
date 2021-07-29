test_case = int(input())

for i in range(1, test_case + 1):
    number = int(input())
    total = 0
    for num in range(1, number + 1):
        if num % 2:
            total += num
        else:
            total -= num

    print('#{} {}'.format(i, total))
