test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    s = input().strip()
    stack = []
    bracket = {'}': '{', ')': '('}
    result = 1
    for letter in s:
        if letter == '{' or letter == '(':
            stack.append(letter)
        elif letter == '}' or letter == ')':
            if not stack or stack[-1] != bracket.get(letter):
                result = 0
                break
            else:
                stack.pop()

    if stack:
        result = 0

    print('#{} {}'.format(t, result))
