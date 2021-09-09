test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    letters = input().strip()
    h_num = int(input().strip())
    locations = list(map(int, input().strip().split()))

    h = [''] * (len(letters) + 1)
    for location in locations:
        h[location] += '-'

    result = ''
    for i in range(len(letters)):
        result += h[i] + letters[i]
    result += h[-1]

    print('#{} {}'.format(t, result))
