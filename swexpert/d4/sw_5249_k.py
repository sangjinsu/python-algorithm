# 최소 신장 트리
# 크루스갈 버전

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


def kruskal(edges):
    edges.sort()

    mst = []
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            mst.append(cost)
    return mst


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    V, E = map(int, input().strip().split())
    edges = []
    parent = [i for i in range(V + 1)]
    for i in range(E):
        u, v, w = map(int, input().strip().split())
        edges.append((w, u, v))

    result = sum(kruskal(edges))

    print('#{} {}'.format(t, result))
