test_cases = int(input())

for t in range(1, test_cases + 1):
    line = input()
    letters = dict()
    for char in line:
        letters.setdefault(char, 0)
        letters[char] += 1

    check = True
    if len(letters.keys()) != 2:
        check = False
    else:
        for value in letters.values():
            if value != 2:
                check = False
    result = 'Yes' if check else 'No'
    print('#{} {}'.format(t, result))
