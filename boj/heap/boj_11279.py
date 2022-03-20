import heapq
import sys

N = int(sys.stdin.read())

heap = []

for _ in range(N):
    num = int(sys.stdin.read())
    if num != 0:
        heapq.heappush(heap, -num)
    else:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))