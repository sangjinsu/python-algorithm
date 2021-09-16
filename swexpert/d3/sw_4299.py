test_cases = int(input().strip())

d = 60 * 24
h = 60
for t in range(1, test_cases + 1):
    blind_day = 11
    blind_hour = 11
    blind_minute = 11

    day, hour, minute = map(int, input().strip().split())

    result = 0
    if day == 11 and hour < 11:
        result = -1
    elif day == 11 and hour == 11 and minute < 11:
        result = -1
    else:
        if blind_minute > minute:
            hour -= 1
            minute += 60

        if blind_hour > hour:
            day -= 1
            hour += 24

        result_day = day - blind_day
        result_hour = hour - blind_hour
        result_minute = minute - blind_minute

        result = result_day * d + result_hour * h + result_minute

    print('#{} {}'.format(t, result))
