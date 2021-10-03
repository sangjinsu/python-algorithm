import sys


def recursion(day, pay):
    global max_pay
    if day >= N:
        max_pay = max(max_pay, pay)
        return

    recursion(day + 1, pay)
    if day + nums[day][0] <= N:
        recursion(day + nums[day][0], pay + nums[day][1])


N = int(sys.stdin.readline().strip())
nums = [0] * N
for i in range(N):
    nums[i] = tuple(map(int, sys.stdin.readline().strip().split()))
max_pay = -1
recursion(0, 0)
sys.stdout.write(str(max_pay))
