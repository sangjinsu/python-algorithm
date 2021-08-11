import sys


def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)


n, s = tuple(map(int, sys.stdin.readline().strip().split()))

distances = list(map(lambda pos: abs(int(pos) - s), sys.stdin.readline().strip().split()))

result = 0
if len(distances) == 1:
    result = distances[0]
else:
    result = gcd(distances[0], distances[1])
    for i in range(2, len(distances)):
        result = gcd(result, distances[i])

sys.stdout.write(str(result))
