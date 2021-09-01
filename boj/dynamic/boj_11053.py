import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

sys.stdout.write(str(max(dp)))
