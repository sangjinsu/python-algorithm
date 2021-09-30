test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    A, B = map(int, input().strip().split())
    N = A // B
    # 등차수열의 합
    result = N * (2 * 1 + (N - 1) * 2) // 2
    print('#{} {}'.format(t, result))
