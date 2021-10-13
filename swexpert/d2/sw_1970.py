test_cases = int(input().strip())

m = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for t in range(1, test_cases + 1):
    money = int(input().strip())
    answer = [''] * 8

    for i in range(8):
        answer[i] = str(money // m[i])
        money = money % m[i]

    print(f'#{t}')
    print(' '.join(answer))
