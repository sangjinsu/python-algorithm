import sys


def recursion(cnt, result):
    if cnt == M:
        sys.stdout.write(result + '\n')
        return
    for i in range(1, N + 1):
        if str(i) not in result:
            recursion(cnt + 1, result + str(i) + ' ')


N, M = map(int, sys.stdin.readline().strip().split())
recursion(0, '')
