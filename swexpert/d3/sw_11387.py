test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    D, L, N = map(int, input().strip().split())
    result = 0
    for i in range(N):
        result += D * (1 + i * L * 0.01)

    print('#{} {}'.format(t, int(result)))
