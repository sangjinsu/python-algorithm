import math

INF = math.inf
test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, A, B = map(int, input().strip().split())

    result = INF
    for R in range(1, N // 2 + 1):
        for C in range(1, N // R + 1):
            result = min(result, A * abs(R - C) + B * (N - R * C))
    print('#{} {}'.format(t, result))
