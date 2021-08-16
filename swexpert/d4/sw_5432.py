test_cases = int(input())

for t in range(1, test_cases + 1):
    brackets = input()
    sticks = -1
    result = 0
    for i in range(len(brackets)):
        if brackets[i] == '(':
            sticks += 1
        else:
            if brackets[i-1] == '(':
                result += sticks
                sticks -= 1
            else:
                result += 1
                sticks -= 1

    print('#{} {}'.format(t, result))
