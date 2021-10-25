def recursion(day, value):
    global result
    if day >= N:
        result = max(result, value)
        return
    recursion(day + 1, value)
    if day + TP[day][0] <= N:
        recursion(day + TP[day][0], value + TP[day][1])


N = int(input().strip())

TP = []
for i in range(N):
    TP.append(tuple(map(int, input().strip().split())))

result = 0
recursion(0, 0)

print(result)
