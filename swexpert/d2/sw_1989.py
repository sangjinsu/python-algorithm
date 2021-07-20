T = int(input())

for test_case in range(1, T + 1):
    letters = input()
    left = 0
    right = len(letters) - 1

    result = 1
    while left <= right:
        if letters[left] != letters[right]:
            result = 0
            break
        left += 1
        right -= 1

    print('#{} {}'.format(test_case, result))
