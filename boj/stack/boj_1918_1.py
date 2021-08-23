import sys


def make_postfix(expr):
    op = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    stack = []
    postfix = ''
    for e in expr:
        if 'A' <= e <= 'Z':
            postfix += e
        else:
            if e == '(':
                stack.append(e)
            elif e == ')':
                while stack and stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            else:
                while stack and op[e] <= op[stack[-1]]:
                    postfix += stack.pop()
                stack.append(e)
    while stack:
        postfix += stack.pop()

    return postfix


expression = sys.stdin.readline().strip()
result = make_postfix(expression)

sys.stdout.write(result)
