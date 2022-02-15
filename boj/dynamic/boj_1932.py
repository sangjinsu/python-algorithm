n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dp[0][0] = mat[0][0]

for i in range(n - 1):
    for j in range(len(mat[i])):
        dp[i + 1][j] = max(dp[i + 1][j], mat[i + 1][j] + dp[i][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], mat[i + 1][j + 1] + dp[i][j])
print(max(dp[n - 1]))
