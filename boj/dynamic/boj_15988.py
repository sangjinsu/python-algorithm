import sys

test_cases = int(sys.stdin.readline().strip())

dp = [0] * 1_000_001
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1_000_001):
    dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1_000_000_009

for t in range(test_cases):
    n = int(sys.stdin.readline().strip())
    sys.stdout.write(str(dp[n]) + '\n')
