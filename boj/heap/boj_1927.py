import heapq

N = int(input())

heap = []

for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
