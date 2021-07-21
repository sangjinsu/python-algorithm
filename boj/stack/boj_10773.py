import sys

k = int(sys.stdin.readline().strip())

stack = list()

for i in range(k):
    item = int(sys.stdin.readline().strip())

    if item == 0:
        stack.pop()
    else:
        stack.append(item)

total = 0
for i in stack:
    total += i

sys.stdout.write(str(total))
