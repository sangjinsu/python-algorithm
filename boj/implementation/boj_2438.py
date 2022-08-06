import sys

N = int(sys.stdin.readline().strip())
[sys.stdout.write('*' * i + '\n') for i in range(1, N + 1)]
