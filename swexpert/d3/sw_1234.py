test_cases = 10

for t in range(1, test_cases + 1):
    test_num, pwd = input().strip().split()
    stack = [pwd[0]]
    for i in range(1, len(pwd)):
        if stack and stack[-1] == pwd[i]:
            stack.pop()
        else:
            stack.append(pwd[i])

    print('#{} {}'.format(t, ''.join(stack)))
