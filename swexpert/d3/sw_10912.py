test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    letters = sorted(list(input().strip()))
    stack = []

    for letter in letters:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)

    result = ''
    if not stack:
        result = 'Good'
    else:
        result = ''.join(stack)

    print('#{} {}'.format(t, result))
