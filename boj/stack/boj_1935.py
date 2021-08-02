import sys

N = int(sys.stdin.readline().strip())

expression = sys.stdin.readline().strip()

nums = dict()
for expr in expression:
    if expr not in '*+-/' and expr not in nums:
        nums[expr] = int(sys.stdin.readline().strip())


stack = list()
for expr in expression:
    if expr not in '*+-/':
        stack.append(nums[expr])
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        value = 0
        if expr == '+':
            value = num2 + num1
        elif expr == '-':
            value = num2 - num1
        elif expr == '*':
            value = num2 * num1
        elif expr == '/':
            value = num2 / num1

        stack.append(value)

sys.stdout.write(f'{stack.pop():.2f}')
