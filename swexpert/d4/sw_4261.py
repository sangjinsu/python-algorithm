phone = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    S, N = input().strip().split()
    words = input().strip().split()

    letters = []
    for num in S:
        letters.append(phone[num])

    result = 0
    for word in words:
        check = 1
        if len(word) != len(letters):
            continue
        for i in range(len(word)):
            if word[i] not in letters[i]:
                check = 0
                break
        result += check
    print('#{} {}'.format(t, result))
