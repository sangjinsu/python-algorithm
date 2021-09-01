test_cases = int(input().strip())

for t in range(1, test_cases+1):
    n, a, b = map(int, input().strip().split())

    max_num = min(a, b)
    min_num = max(a + b - n, 0)

    print('#{} {} {}'.format(t, max_num, min_num))
