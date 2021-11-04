from collections import deque


def make_postfix(expr):
    postfix = ''
    stack = deque()
    for e in expr:
        if '0' <= e <= '9':
            postfix += e
        else:
            if stack:
                postfix += stack.pop()
            stack.append(e)
    for s in stack:
        postfix += s
    return postfix


def solve(postfix):
    stack = deque()
    for n in postfix:
        if '0' <= n <= '9':
            stack.append(int(n))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num1 + num2)
    return stack[0]


test_cases = 10
for t in range(1, test_cases + 1):
    N = input()
    expr = input().strip()
    postfix = make_postfix(expr)
    print('#{} {}'.format(t, solve(postfix)))
