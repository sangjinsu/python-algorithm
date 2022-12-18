import sys
from itertools import combinations

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().strip().split()))
nums.sort()

start, end = 0, N - 1
total = 0
result = 0

while start < end:
    total = nums[start] + nums[end]
    if total == M:
        result += 1
        start += 1
        end -= 1
    elif total > M:
        end -= 1
    elif total < M:
        start += 1

sys.stdout.write(str(result))
