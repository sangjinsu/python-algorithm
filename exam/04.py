from collections import deque


def solution(n, k, bulbs):
    change = {
        'R': 'G',
        'G': 'B',
        'B': 'R',
    }

    answer = -1
    redBulbs = 'R' * n
    d = dict()

    def bfs():
        nonlocal answer
        queue = deque()
        S = set()
        queue.append([bulbs, 0])
        while queue:
            b, cnt = queue.popleft()
            print(b, d)
            if b == redBulbs:
                answer = cnt
                return
            for i in range(n - k + 1):
                temp = list(bulbs)
                for j in range(i, i + k):
                    temp[j] = change[temp[j]]
                    changed = ''.join(temp)
                    if d.get(changed, 1):
                        queue.append([changed, cnt + 1])
                        d[changed] = 1

    bfs()

    return answer


solution(3, 2, "BGG")
