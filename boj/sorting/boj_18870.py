import sys
import bisect

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))

indices = sorted(list(set(nums)))
for num in nums:
    sys.stdout.write(str(bisect.bisect_left(indices, num)) + ' ')
