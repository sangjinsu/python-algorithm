import math


def solution(progresses, speeds):
    answer = []

    days = []
    for i in range(len(progresses)):
        day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(day)

    k = days[0]
    d = 1
    for i in range(1, len(days)):
        if k >= days[i]:
            d += 1
        else:
            k = days[i]
            answer.append(d)
            d = 1
    answer.append(d)
    return answer


progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
