test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    letters = input().strip()
    stack = [letters[0]]

    for i in range(1, len(letters)):
        if stack and stack[-1] == letters[i]:
            stack.pop()
        else:
            stack.append(letters[i])

    print('#{} {}'.format(t, len(stack)))
    