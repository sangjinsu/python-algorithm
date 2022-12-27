import sys

n = int(sys.stdin.readline().strip())

nums = []
for i in range(n):
    nums.append(int(sys.stdin.readline().strip()))

nums.sort()
for num in nums:
    sys.stdout.write(str(num) + '\n')
