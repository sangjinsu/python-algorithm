import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums: list[int] = list(map(int, sys.stdin.readline().strip().split()))
temp = 0
s = [0] * (N + 1)

for i in range(N):
    temp = temp + nums[i]
    s[i + 1] = temp

for i in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    sys.stdout.write(str(s[end] - s[start - 1]) + '\n')
