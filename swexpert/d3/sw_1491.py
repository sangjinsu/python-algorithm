test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, A, B = map(int, input().strip().split())

    result = 10 ** 9
    for R in range(1, int(N ** 0.5) + 1):
        for C in range(R, N // R + 1):
            result = min(result, A * abs(R - C) + B * (N - R * C))
    print('#{} {}'.format(t, result))
