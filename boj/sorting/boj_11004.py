import sys

n, k = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

nums.sort()
sys.stdout.write(str(nums[k - 1]))
