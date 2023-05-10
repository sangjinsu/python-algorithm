import sys
import heapq

def solve():
    n = int(sys.stdin.readline().strip())
    pq = list()
    for _ in range(n):
        num = int(sys.stdin.readline().strip())
        if num != 0:
            heapq.heappush(pq, (abs(num), num))
        else:
            if pq:
                sys.stdout.write(str(heapq.heappop(pq)[1]) + '\n')
            else:
                sys.stdout.write(str(0) + '\n')


if __name__ == '__main__':
    solve()
