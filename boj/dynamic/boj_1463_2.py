N = int(input().strip())

dp = [10 ** 6 + 1] * (N + 1)
dp[0] = 0
dp[1] = 0

for i in range(N + 1):
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[N])
