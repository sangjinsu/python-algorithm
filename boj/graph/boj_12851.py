import sys
import math
from collections import deque


def bfs(n):
    queue = deque()
    queue.append(n)
    result = 0
    min_cnt = math.inf
    while queue:
        num = queue.popleft()

        if num == K:
            print(num, sec[num])
            min_cnt = sec[num]
            result += 1

        for k in [num + 1, num - 1, num * 2]:
            if 0 <= k <= 100_000 and not sec[k]:
                queue.append(k)
                sec[k] = sec[num] + 1
    return min_cnt, result


N, K = map(int, sys.stdin.readline().strip().split())
sec = [0] * (100_000 + 1)
c, r = bfs(N)
sys.stdout.write(str(c) + '\n')
sys.stdout.write(str(r) + '\n')
