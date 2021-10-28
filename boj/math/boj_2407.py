import sys


def factorial(k, m):
    result = 1
    for i in range(m, k + 1):
        result *= i
    return result


n, m = map(int, sys.stdin.readline().strip().split())

result = factorial(n, n - m + 1) // factorial(m, 1)
sys.stdout.write(str(result))
