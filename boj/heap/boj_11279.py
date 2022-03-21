import heapq
import sys

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        if not heap:
            sys.stdout.write(str(0) + '\n')
        else:
            sys.stdout.write(str(-heapq.heappop(heap)) + '\n')
