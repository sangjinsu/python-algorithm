import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

nums_sorted = sorted(nums)
minutes = [0] * n
minutes[0] = nums_sorted[0]

for i in range(1, n):
    minutes[i] = minutes[i - 1] + nums_sorted[i]

sys.stdout.write(str(sum(minutes)))
