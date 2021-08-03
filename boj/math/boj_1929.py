import sys

num1, num2 = map(int, sys.stdin.readline().strip().split())

nums = [True] * (num2 + 1)

nums[0] = False
nums[1] = False

m = int(num2 ** 0.5)
for i in range(2, m + 1):
    if nums[i]:
        for j in range(2 * i, num2 + 1, i):
            nums[j] = False

for i in range(num1, num2 + 1):
    if nums[i]:
        sys.stdout.write(str(i) + '\n')
