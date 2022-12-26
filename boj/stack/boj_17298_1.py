import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

result = [0] * n
stack = []

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        result[stack.pop()] = nums[i]

    stack.append(i)

while stack:
    result[stack.pop()] = -1

print(*result)



