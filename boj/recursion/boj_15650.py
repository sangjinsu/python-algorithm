import sys


def recursion(cnt, result):
    if cnt == M:
        sys.stdout.write(result + '\n')
        return
    start = int(result[-2]) if result else 1
    for i in range(start, N + 1):
        if str(i) not in result:
            recursion(cnt + 1, result + str(i) + ' ')


N, M = map(int, sys.stdin.readline().strip().split())
recursion(0, '')
