import sys


def recursion(k):
    global cnt
    if k == N:
        cnt += 1
        if command == 1 and cnt == collect[0]:
            for i in t:
                sys.stdout.write(str(i) + ' ')
            sys.stdout.write('\n')
        if command == 2 and t == collect:
            sys.stdout.write(str(cnt))
        return
    else:
        for i in range(1, N + 1):
            if not visited[i]:
                t[k] = i
                visited[i] = True
                recursion(k + 1)
                visited[i] = False


N = int(sys.stdin.readline().strip())
command, *collect = map(int, input().strip().split())
visited = [False] * (N + 1)
t = [0] * N
cnt = 0
recursion(0)
