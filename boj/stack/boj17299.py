import sys

n = sys.stdin.readline().strip()

numbers = list(map(int, sys.stdin.readline().strip().split()))

f = dict()

for number in numbers:
    f.setdefault(number, 0)
    f[number] += 1

stack = list()
result = ['-1'] * len(numbers)
for i, number in enumerate(numbers):
    while stack and f[numbers[stack[-1]]] < f[number]:
        result[stack[-1]] = str(number)
        stack.pop()
    stack.append(i)

sys.stdout.write(' '.join(result))
