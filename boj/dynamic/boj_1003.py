test_case = int(input())


def fibo(N):
    zero = [0] * 41
    one = [0] * 41

    zero[0] = 1
    one[1] = 1

    for i in range(2, N + 1):
        zero[i] = zero[i - 1] + zero[i - 2]
        one[i] = one[i - 1] + one[i - 2]

    return zero[N], one[N]


for t in range(test_case):
    N = int(input())
    print(*fibo(N))
