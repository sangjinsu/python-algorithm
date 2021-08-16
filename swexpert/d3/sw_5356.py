test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    columns = [''] * 15
    for i in range(5):
        letters = input().strip()
        for j in range(len(letters)):
            columns[j] += letters[j]
    print('#{} {}'.format(t, ''.join(columns)))