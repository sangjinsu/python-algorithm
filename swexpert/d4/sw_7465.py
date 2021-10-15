test_cases = int(input().strip())


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


for t in range(1, test_cases + 1):
    N, M = map(int, input().strip().split())
    parent = [i for i in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().strip().split())
        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
    group = 0
    for i in range(1, N + 1):
        if parent[i] == i:
            group += 1
    print('#{} {}'.format(t, group))
