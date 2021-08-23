test_cases = 10


def make_postfix(expr):
    op = {
        '(': 0,
        '+': 1,
        '*': 2,
    }

    stack = []
    postfix = ''
    for e in expr:
        if '0' <= e <= '9':
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


def solve_postfix(pf):
    stack = []
    for e in pf:
        if '0' <= e <= '9':
            stack.append(int(e))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if e == '+':
                stack.append(num1 + num2)
            elif e == '*':
                stack.append(num1 * num2)

    return stack[0]


for t in range(1, test_cases + 1):
    length = int(input().strip())
    expression = input().strip()
    postfix = make_postfix(expression)
    result = solve_postfix(postfix)
    print('#{} {}'.format(t, result))
