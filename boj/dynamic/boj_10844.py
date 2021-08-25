import sys
from pprint import pprint

n = int(sys.stdin.readline().strip())

dp = [[0] * 10 for _ in range(n + 1)]
dp[1] = [1] * 10

mod = 1_000_000_000
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][j + 1]
        elif 1 <= j <= 8:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        else:
            dp[i][j] = dp[i - 1][j - 1]

result = sum(dp[n][1:]) % mod
sys.stdout.write(str(result))
