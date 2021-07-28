import sys

n = sys.stdin.readline().strip()

numbers = list(map(int, sys.stdin.readline().strip().split()))

stack = [0]

result = ['-1'] * len(numbers)

for i in range(1, len(numbers)):
    while stack and numbers[stack[-1]] < numbers[i]:
        result[stack[-1]] = str(numbers[i])
        stack.pop()
    stack.append(i)

sys.stdout.write(' '.join(result))
