class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def inorder(n):
    global expr
    if n is not None:
        inorder(tree[n].left)
        expr += tree[n].value
        inorder(tree[n].right)


test_cases = 10
for t in range(1, test_cases + 1):
    N = int(input())
    tree = [Node() for _ in range(N + 1)]

    for _ in range(N):
        inputs = input().split()
        idx = int(inputs[0])
        value = inputs[1]
        args = inputs[2:]

        tree[idx].value = value
        if len(args) == 2:
            tree[idx].left = int(args[0])
            tree[idx].right = int(args[1])
    expr = ''
    inorder(1)

    result = 1
    for i in range(0, len(expr) - 1, 2):
        if expr[i + 1] not in '+-*/' or not expr[i].isdigit():
            result = 0
            break
    if not expr[len(expr) - 1].isdigit():
        result = 0

    print('#{} {}'.format(t, result))
