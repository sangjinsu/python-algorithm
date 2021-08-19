import sys

n = int(sys.stdin.readline().strip())
dp = [1] * (n+1)

for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]*2

sys.stdout.write(str(dp[-1] % 10007))
