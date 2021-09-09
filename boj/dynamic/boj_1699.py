import sys

n = int(sys.stdin.readline())
dp = [i for i in range(n + 1)]

for i in range(1, n + 1):
    num = 2
    while i >= num * num:
        if dp[i] > dp[i - num * num] + 1:
            dp[i] = dp[i - num * num] + 1
        num += 1

sys.stdout.write(str(dp[-1]))
