test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    string = input().strip()

    result = 'Exist'
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            if string[left] != '?' and string[right] != '?':
                result = 'Not exist'
                break
        left += 1
        right -= 1
    print('#{} {}'.format(t, result))
