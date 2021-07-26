T = int(input())

for i in range(1, T + 1):
    word = input().strip()
    result = ''
    for letter in word:
        if letter not in 'aeiou':
            result += letter
    print('#{} {}'.format(i, result))
