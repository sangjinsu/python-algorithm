# 그룹 나누기

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
    N, M = map(int, input().strip().split())
    parent = [i for i in range(N + 1)]
    req = list(map(int, input().strip().split()))
    for i in range(M):
        a, b = req[i * 2], req[i * 2 + 1]
        union_parent(parent, a, b)

    group = set()
    for p in parent:
        group.add(find_parent(parent, p))

    print('#{} {}'.format(t, len(group) - 1))
