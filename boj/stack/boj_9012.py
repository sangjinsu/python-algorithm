test_case = int(input())

for i in range(test_case):
    brackets = input()
    stack = 0
    answer = 'YES'
    for bracket in brackets:
        if bracket == '(':
            stack += 1
        else:
            if stack == 0:
                answer = 'NO'
                break
            stack -= 1

    if stack > 0:
        answer = 'NO'

    print(answer)
