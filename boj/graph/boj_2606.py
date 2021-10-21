import sys


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(sys.stdin.readline().strip())
E = int(sys.stdin.readline().strip())
parent = [i for i in range(N + 1)]
for _ in range(E):
    a, b = map(int, input().strip().split())
    union(parent, a, b)

result = -1
for p in range(1, len(parent)):
    if find_parent(parent, p) == 1:
        result += 1
sys.stdout.write(str(result))
