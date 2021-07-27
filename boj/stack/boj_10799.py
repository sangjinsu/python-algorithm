import sys

brackets = sys.stdin.readline().strip()

sticks = -1
result = 0
for i, bracket in enumerate(brackets):
    if bracket == '(':
        sticks += 1
    else:
        if brackets[i-1] == '(':
            result += sticks
            sticks -= 1
        else:
            sticks -= 1
            result += 1

sys.stdout.write(str(result))
