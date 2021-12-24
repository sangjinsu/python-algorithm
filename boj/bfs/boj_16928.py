from collections import deque

N, M = map(int, input().split())

path = dict()
for i in range(N + M):
    a, b = map(int, input().split())
    path[a] = b

queue = deque([(1, 0)])
visited = [False] * 101

while queue:
    pos, cnt = queue.popleft()
    visited[pos] = True

    if pos == 100:
        print(cnt)
        break

    for i in range(1, 7):
        np = pos + i
        if np > 100:
            break
        if path.get(np, 0):
            np = path[np]
        if not visited[np]:
            queue.append((np, cnt + 1))
