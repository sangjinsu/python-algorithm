import sys

n = int(sys.stdin.readline().strip())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 2] + dp[i - 1]

sys.stdout.write(str(dp[-1] % 10007))
