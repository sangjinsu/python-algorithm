import sys
from queue import PriorityQueue

n = int(sys.stdin.readline().strip())
pq = PriorityQueue()
li = list()
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get()[-1])
    else:
        pq.put((abs(num), num))

