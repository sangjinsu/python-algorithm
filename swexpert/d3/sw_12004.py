test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N = int(input().strip())
    result = 'No'
    for i in range(1, 10):
        num = N / i
        if num == int(num) and 1 <= num <= 9:
            result = 'Yes'
            break
    print('#{} {}'.format(t, result))
