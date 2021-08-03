test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n, m = tuple(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    result = 0
    if n <= m:
        for i in range(m - n + 1):
            temp = 0
            for j in range(n):
                temp += a[j] * b[j + i]
            result = max(result, temp)
    else:
        for i in range(n - m + 1):
            temp = 0
            for j in range(m):
                temp += a[j + i] * b[j]
            result = max(result, temp)

    print('#{} {}'.format(t, result))
