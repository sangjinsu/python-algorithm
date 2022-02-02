import sys
from collections import deque

test_cases = int(input())


def bfs(v):
    queue = deque([(v, '')])
    visited = set()
    visited.add(v)
    while queue:
        value, n = queue.popleft()

        if value == B:
            return n

        D = value * 2
        if D > 9999:
            D %= 10000
        if D not in visited:
            visited.add(D)
            queue.append((D, n + 'D'))

        S = value
        if S == 0:
            S = 9999
        else:
            S -= 1
        if S not in visited:
            visited.add(S)
            queue.append((S, n + 'S'))

        L = (value % 1000 * 10) + (value // 1000)
        if L not in visited:
            visited.add(L)
            queue.append((L, n + 'L'))

        R = (value % 10 * 1000) + (value // 10)
        if R not in visited:
            visited.add(R)
            queue.append((R, n + 'R'))


for t in range(1, test_cases + 1):
    A, B = map(int, sys.stdin.readline().strip().split())
    sys.stdout.write(str(bfs(A)) + '\n')
