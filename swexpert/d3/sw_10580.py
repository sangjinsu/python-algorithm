test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    N = int(input().strip())
    power_pole_1 = []
    power_pole_2 = []

    for i in range(N):
        line1, line2 = map(int, input().strip().split())
        power_pole_1.append(line1)
        power_pole_2.append(line2)

    cnt = 0
    for i in range(N):
        line1 = power_pole_1[i]
        line2 = power_pole_2[i]
        for j in range(N):
            if power_pole_2[j] < line2 and power_pole_1[j] > line1:
                cnt += 1
            if power_pole_2[j] > line2 and power_pole_1[j] < line1:
                cnt += 1

    print('#{} {}'.format(t, cnt // 2))
