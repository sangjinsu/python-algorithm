import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    stack = sys.stdin.readline().strip().split()

    answer = f'Case #{i + 1}:'
    while len(stack) > 0:
        word = stack.pop()
        answer += ' ' + word

    sys.stdout.write(answer + '\n')
