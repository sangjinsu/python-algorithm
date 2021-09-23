class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def calc(expr):
    if expr in '+-*/':
        num2 = stack.pop()
        num1 = stack.pop()
        if expr == '+':
            stack.append(num1 + num2)
        elif expr == '-':
            stack.append(num1 - num2)
        elif expr == '*':
            stack.append(num1 * num2)
        elif expr == '/':
            stack.append(num1 / num2)
    else:
        stack.append(int(expr))


def post_order(n):
    if n is not None:
        post_order(tree[n].left)
        post_order(tree[n].right)
        calc(tree[n].value)


test_cases = 10
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

    stack = []
    post_order(1)
    print('#{} {}'.format(t, int(stack[0])))
