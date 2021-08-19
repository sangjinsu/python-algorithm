import sys

test_cases = int(sys.stdin.readline().strip())

for t in range(test_cases):
    n = int(sys.stdin.readline().strip())
    dp = [0] * 11
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 11):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

    sys.stdout.write(str(dp[n])+'\n')
