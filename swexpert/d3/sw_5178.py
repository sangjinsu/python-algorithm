# 노드의 합
test_cases = int(input())

for t in range(1, test_cases + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        node, value = map(int, input().split())
        tree[node] = value

    for i in range(N - M, 0, -1):
        tree[i] = tree[i * 2]
        if i * 2 + 1 <= N:
            tree[i] += tree[i * 2 + 1]

    print('#{} {}'.format(t, tree[L]))
