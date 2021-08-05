test_cases = int(input())

for i in range(1, test_cases + 1):
    sentence = input()
    cnt = 1
    while True:
        # print(sentence[:cnt], sentence[cnt:2 * cnt])
        if sentence[:cnt] == sentence[cnt:2 * cnt]:
            break
        cnt += 1
        if cnt > 10:
            break
    print('#{} {}'.format(i, cnt))
