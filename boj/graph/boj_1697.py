from collections import deque


def bfs(N, M):
    queue = deque()
    queue.append(N)
    while queue:
        num = queue.popleft()
        if num == M:
            return sec[num]
        for n in [num + 1, num - 1, num * 2]:
            if 0 <= n <= 100_000 and not sec[n]:
                sec[n] = sec[num] + 1
                queue.append(n)


N, M = map(int, input().strip().split())
sec = [0] * (100_000 + 1)
print(bfs(N, M))
