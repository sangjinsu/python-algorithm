import sys

n, m = map(int, sys.stdin.readline().strip().split())
cant_hear = set([sys.stdin.readline().strip() for _ in range(n)])
cant_see = set([sys.stdin.readline().strip() for _ in range(m)])

result = cant_hear.intersection(cant_see)

sys.stdout.write(str(len(result)) + '\n')
for name in sorted(list(result)):
    sys.stdout.write(name + '\n')


