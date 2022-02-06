x = int(input())

dp = [10 ** 6 + 1] * (x + 1)
dp[0] = 0
dp[1] = 0

for i in range(2, len(dp)):
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    dp[i] = min(dp[i], dp[i - 1] + 1)
print(dp[-1])
