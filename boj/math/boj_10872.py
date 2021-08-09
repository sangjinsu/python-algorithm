import sys


def factorial(n):
    if n <= 1:
        return 1
    return factorial(n - 1) * n


n = int(sys.stdin.readline().strip())

result = factorial(n)

sys.stdout.write(str(result))
