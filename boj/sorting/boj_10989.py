import sys

n = int(sys.stdin.readline().strip())
counts = [0] * 10_001

for _ in range(n):
    counts[int(sys.stdin.readline().strip())] += 1

for i in range(len(counts)):
    if counts[i]:
        for _ in range(counts[i]):
            sys.stdout.write(str(i) + '\n')
