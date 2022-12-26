import sys
from collections import deque

n = int(sys.stdin.readline().strip())
queue = deque([i for i in range(n, 0, -1)])

while len(queue) > 1:
    queue.pop()
    queue.appendleft(queue.pop())

print(queue[0])
