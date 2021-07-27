for t in range(1, 3):
    test_length = int(input().strip())
    case = input()
    stack = list()
    postfix = ''

    prec = {
        '*': 3,
        '+': 2,
        '(': 1
    }

    for i in range(test_length):
        if case[i] in '+*)(':
            if case[i] == '(':
                stack.append('(')
            elif case[i] == ')':
                while stack[-1] != '(':
                    postfix += stack.pop()
                stack.pop()
            else:
                while stack and prec[case[i]] <= prec[stack[-1]]:
                    postfix += stack.pop()
                stack.append(case[i])
        else:
            postfix += case[i]

    while len(stack) > 0:
        postfix += stack.pop()

    for i in range(len(postfix)):
        if postfix[i] not in '+*':
            stack.append(int(postfix[i]))
        else:
            if postfix[i] == '*':
                stack.append(stack.pop() * stack.pop())
            elif postfix[i] == '+':
                stack.append(stack.pop() + stack.pop())

    print('#{} {}'.format(t, stack[0]))
