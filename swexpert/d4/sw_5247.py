# 연산
# queue 사용시 시간 초과
# 백트래킹 사용시 시간 초과
from collections import deque


def BFS(n, cnt):
    queue = deque([(n, cnt)])

    while queue:
        num, cnt = queue.popleft()
        if nums.get(num, 0):
            continue
        nums[num] = 1

        if num == M:
            return cnt
        if 0 < num + 1 <= 1_000_000:
            queue.append((num + 1, cnt + 1))
        if 0 < num * 2 <= 1_000_000:
            queue.append((num * 2, cnt + 1))
        if 0 < num - 1 <= 1_000_000:
            queue.append((num - 1, cnt + 1))
        if 0 < num - 10 <= 1_000_000:
            queue.append((num - 10, cnt + 1))


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())
    nums = dict()
    max_cnt = BFS(N, 0)
    print('#{} {}'.format(t, max_cnt))
