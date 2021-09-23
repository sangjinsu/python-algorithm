test_cases = 10


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder(n):
    if n is not None:
        inorder(tree[n].left)
        print(tree[n].value, end='')
        inorder(tree[n].right)


for t in range(1, test_cases + 1):
    n = int(input())
    tree = [Node() for _ in range(n + 1)]

    for _ in range(n):
        idx, value, *args = input().split()
        idx = int(idx)

        tree[idx].value = value
        if len(args) == 2:
            tree[idx].left = int(args[0])
            tree[idx].right = int(args[1])
        elif len(args) == 1:
            tree[idx].left = int(args[0])

    print('#{}'.format(t), end=' ')
    inorder(1)
    print()
