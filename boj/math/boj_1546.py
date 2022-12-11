import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
M = max(nums)
scores = [num/M*100 for num in nums]

sys.stdout.write(str(sum(scores)/N))
