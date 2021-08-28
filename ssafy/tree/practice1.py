v = int(input().strip())
edge = list(map(int, input().strip().split()))
e = v - 1

tree = [[0] * 2 for _ in range(v + 1)]

for i in range(e):
    p, c = edge[i * 2], edge[i * 2 + 1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c


def preorder0(root):
    if root != 0:
        print(root)
        preorder0(tree[root][0])
        preorder0(tree[root][1])


preorder0(1)


def preorder(root):
    if root <= N:
        print(root, tree[root])
        preorder(root * 2)
        preorder(root * 2 + 1)


def preorder2(root):
    print(root, tree[root])
    if root * 2 <= N:
        preorder2(root * 2)
    if root * 2 + 1 <= N:
        preorder2(root * 2 + 1)


N = 10
tree = [i * 100 for i in range(N + 1)]
preorder(1)
