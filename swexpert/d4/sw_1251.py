# 크루스갈
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    island = int(input().strip())
    pos_x = list(map(int, input().strip().split()))
    pos_y = list(map(int, input().strip().split()))
    E = float(input().strip())
    edges = []
    for i in range(island - 1):
        for j in range(i + 1, island):
            if i != j:
                length = abs(pos_x[i] - pos_x[j]) ** 2 + abs(pos_y[i] - pos_y[j]) ** 2
                edges.append((length, i, j))
    parent = [i for i in range(island + 1)]

    edges.sort()
    result = 0
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost
    print('#{} {}'.format(t, round(result * E)))
