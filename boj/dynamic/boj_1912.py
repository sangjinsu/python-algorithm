import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
dp = [0] * n
dp[0] = nums[0]
for i in range(1, n):
    dp[i] = max(nums[i], dp[i - 1] + nums[i])

sys.stdout.write(str(max(dp)))
  