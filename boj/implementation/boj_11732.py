import sys

M = int(sys.stdin.readline().strip())

numSet = set()

for _ in range(M):
    inputs = sys.stdin.readline().strip().split()
    if len(inputs) == 1:
        command = inputs[0]
    else:
        command, num = inputs
        num = int(num)
    if command == 'add':
        numSet.add(num)
    elif command == 'remove':
        numSet.discard(num)
    elif command == 'check':
        if num in numSet:
            sys.stdout.write('1\n')
        else:
            sys.stdout.write('0\n')
    elif command == 'toggle':
        if num in numSet:
            numSet.discard(num)
        else:
            numSet.add(num)
    elif command == 'all':
        numSet = set([i for i in range(1, 21)])
    elif command == 'empty':
        numSet.clear()
