test_cases = int(input())

for t in range(test_cases):
    n = int(input())
    mat = [list(map(int, input().strip().split())) for _ in range(2)]

    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][1] = mat[0][0]
    dp[1][1] = mat[1][0]

    for i in range(2, n + 1):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + mat[0][i-1]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + mat[1][i-1]

    print(max(dp[0][n], dp[1][n]))
