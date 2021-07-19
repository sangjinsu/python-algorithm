import sys

arr_length = int(sys.stdin.readline())

m = 0
stack = list()
result = list()
for i in range(arr_length):
    num = int(sys.stdin.readline())

    while num > m:
        m += 1
        stack.append(m)
        result.append('+')

    if stack[-1] == num:
        top = stack.pop()
        result.append('-')
    else:
        result = 'NO'
        break

if result == 'NO':
    sys.stdout.write(result)
else:
    sys.stdout.write('\n'.join(result))
