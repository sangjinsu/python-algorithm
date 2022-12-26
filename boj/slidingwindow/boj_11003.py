import sys
from collections import deque

N, L = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().split()))
d = deque()

for i in range(len(nums)):
    num = nums[i]
    while d and d[-1][0] > num:
        d.pop()
    d.append((num, i))
    while d[0][1] <= i - L:
        d.popleft()
    sys.stdout.write(str(d[0][0]) + ' ')
