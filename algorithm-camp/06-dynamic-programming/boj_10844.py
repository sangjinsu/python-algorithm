import sys

if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    dp = [[0] * 10 for _ in range(n + 1)]

    for i in range(1, 10):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                dp[i][j] += dp[i - 1][j + 1]
            elif j == 9:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
            dp[i][j] %= 1_000_000_000

    result = sum(dp[n]) % 1_000_000_000
    sys.stdout.write(str(result))
