pairs = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<',

}

test_cases = 10
for t in range(1, test_cases + 1):
    N = int(input().strip())
    brackets = input().strip()
    stack = []

    result = 1
    for bracket in brackets:
        if bracket in ')]}>':
            if stack[-1] == pairs[bracket]:
                stack.pop()
            else:
                result = 0
                break
        else:
            stack.append(bracket)

    print('#{} {}'.format(t, result))
