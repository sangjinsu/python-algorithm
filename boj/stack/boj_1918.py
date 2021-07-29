import sys

expression = sys.stdin.readline().strip()

op = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

stack = list()
postfix = ''

for expr in expression:
    if expr in '+-*/)(':
        if expr == '(':
            stack.append(expr)
        elif expr == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and op[expr] <= op[stack[-1]]:
                postfix += stack.pop()
            stack.append(expr)
    else:
        postfix += expr

while stack:
    postfix += stack.pop()

sys.stdout.write(postfix)
