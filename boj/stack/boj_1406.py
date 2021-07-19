import sys

chars = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

left = list(chars)
right = list()

for i in range(n):
    instruction = sys.stdin.readline().split()

    if instruction[0] == 'L':
        if len(left):
            item = left.pop()
            right.append(item)

    if instruction[0] == 'D':
        if len(right):
            item = right.pop()
            left.append(item)

    if instruction[0] == 'B':
        if len(left):
            left.pop()

    if instruction[0] == 'P':
        left.append(instruction[1])


right.reverse()
sys.stdout.write(''.join(left) + ''.join(right))
