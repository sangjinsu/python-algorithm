# Forth
test_cases = int(input().strip())


def solve_forth(expr: [str]):
    stack = []
    for e in expr:
        if e.isdecimal():
            stack.append(int(e))
        else:
            if e == '.':
                break
            if len(stack) < 2:
                return 'error'

            num2 = stack.pop()
            num1 = stack.pop()
            if e == '+':
                stack.append(num1 + num2)
            elif e == '-':
                stack.append(num1 - num2)
            elif e == '/':
                stack.append(num1 // num2)
            elif e == '*':
                stack.append(num1 * num2)
    if len(stack) > 1:
        return 'error'

    return stack[-1]


for t in range(1, test_cases + 1):
    expr = input().strip().split()
    result = solve_forth(expr)
    print('#{} {}'.format(t, result))
