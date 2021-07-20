import sys

n, k = tuple(map(int, sys.stdin.readline().split()))

queue = list(range(1, n + 1))
result = list()

i = k - 1
while len(queue):
    item = queue.pop(i)
    result.append(item)
    if len(queue) > 0:
        i = (i + k - 1) % (len(queue))

sys.stdout.write('<{}>'.format(', '.join(map(str, result))))
