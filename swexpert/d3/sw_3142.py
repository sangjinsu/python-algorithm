test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n, m = map(int, input().strip().split())
    cnt = m
    while n != m:
        n -= 2
        m -= 1

    print('#{} {} {}'.format(t, n, cnt-n))
