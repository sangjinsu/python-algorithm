test_case = int(input())

for i in range(test_case):
    sentence = input()
    stack = list()
    answer = ''
    for letter in sentence:
        if letter == ' ':
            while len(stack) > 0:
                answer += stack.pop()
            answer += letter
        else:
            stack.append(letter)

    while len(stack) > 0:
        answer += stack.pop()

    print(answer)
