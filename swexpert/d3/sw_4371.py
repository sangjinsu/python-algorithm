test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    day = [int(input().strip()) for _ in range(N)][1:]

    ship = 0
    while day:
        ship += 1
        max_day = day[-1]
        d = day[0] - 1

        docks = [i for i in range(1 + d, max_day + 1, d) if i in day]
        for dock in docks:
            day.remove(dock)

    print('#{} {}'.format(t, ship))
