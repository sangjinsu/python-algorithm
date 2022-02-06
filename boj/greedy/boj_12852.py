x = int(input())

dp = [[10 ** 6 + 1, i] for i in range(x + 1)]
dp[0] = [0, 0]
dp[1] = [0, 0]

for i in range(2, len(dp)):
    if i % 2 == 0:
        if dp[i][0] > dp[i // 2][0] + 1:
            dp[i][0] = dp[i // 2][0] + 1
            dp[i][1] = i // 2
    if i % 3 == 0:
        if dp[i][0] > dp[i // 3][0] + 1:
            dp[i][0] = dp[i // 3][0] + 1
            dp[i][1] = i // 3

    if dp[i][0] > dp[i - 1][0] + 1:
        dp[i][0] = dp[i - 1][0] + 1
        dp[i][1] = i - 1

print(dp[-1][0])

k = x
while k != 0:
    print(k, end=' ')
    k = dp[k][1]
