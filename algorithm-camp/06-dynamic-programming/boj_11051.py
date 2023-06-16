import sys

sys.setrecursionlimit(10 ** 7)


def recursion(results, n: int, k: int):
    if results.get((n, k)):
        return results.get((n, k))

    if k == 0 or k == n:
        results[(n, k)] = 1
        return results[(n, k)]

    results[(n, k)] = recursion(results, n - 1, k - 1) + recursion(results, n - 1, k)
    return results[(n, k)]


if __name__ == '__main__':
    N, K = map(int, sys.stdin.readline().split())
    results = dict()
    result = recursion(results, N, K) % 10_007
    sys.stdout.write(str(result))
