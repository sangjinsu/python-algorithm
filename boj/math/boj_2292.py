import sys

N = int(sys.stdin.readline().strip())

i, k = 1, 1

while True:
    if N <= k:
        break
    k += 6 * i
    i += 1

sys.stdout.write(str(i))
