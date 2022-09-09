import sys

M, N = map(int, sys.stdin.readline().strip().split())

monsters = dict()
numbers = dict()

for i in range(1, M + 1):
    name = sys.stdin.readline().strip()
    monsters[name] = i
    numbers[i] = name

for _ in range(N):
    value = sys.stdin.readline().strip()
    if value.isnumeric():
        sys.stdout.write(numbers[int(value)] + '\n')
    if value.isalpha():
        sys.stdout.write(str(monsters[value]) + '\n')
