test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N = int(input().strip())
    dp = [0] * (100 + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    for i in range(6, N + 1):
        dp[i] = dp[i - 1] + dp[i - 5]
    print('#{} {}'.format(t, dp[N]))
