test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    str1 = input().strip()
    str2 = input().strip()

    d = dict()
    for letter in str2:
        d.setdefault(letter, 0)
        d[letter] += 1

    max_num = 0
    for i in str1:
        max_num = d.get(i) if d.get(i, 0) > max_num else max_num

    print('#{} {}'.format(t, max_num))
