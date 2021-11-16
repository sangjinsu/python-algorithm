import sys

N = int(sys.stdin.readline().strip())

result = 0
i = 1
while i <= N:
    result += N - i + 1
    i *= 10

sys.stdout.write(str(result))
