import sys


def fib(n: int, memo: dict):
    if n <= 1:
        return n
    if memo.get(n):
        return memo.get(n)
    value = fib(n - 1, memo) + fib(n - 2, memo)
    memo[n] = value
    return value


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    memo = dict()
    sys.stdout.write(str(fib(N, memo)))
