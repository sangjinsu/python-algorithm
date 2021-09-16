import sys

num = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
if n:
    btn = sys.stdin.readline().strip().split()
else:
    btn = []

result = abs(100 - num)

for i in range(1_000_000):
    for j in str(i):
        if j in btn:
            break
    else:
        result = min(result, len(str(i)) + abs(i - num))

sys.stdout.write(str(result))
