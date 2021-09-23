# subtree
class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def inorder(n):
    global cnt

    if n is not None:
        cnt += 1
        inorder(tree[n].left)
        inorder(tree[n].right)


test_cases = int(input())
for t in range(1, test_cases + 1):
    edge, root = map(int, input().split())
    node = edge + 1
    tree = [Node() for _ in range(node + 1)]

    data = list(map(int, input().split()))
    for i in range(len(data)):
        if i % 2 == 0:
            if tree[data[i]].left is None:
                tree[data[i]].left = data[i + 1]
            else:
                tree[data[i]].right = data[i + 1]

    cnt = 0
    inorder(root)

    print('#{} {}'.format(t, cnt))
