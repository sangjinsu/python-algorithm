test_cases = int(input().strip())


def make_primes(num):
    check = [True] * (num + 1)
    m = int(num ** 0.5)
    check[0] = False
    check[1] = False
    for i in range(2, m + 1):
        if check[i]:
            for j in range(i + i, num + 1, i):
                check[j] = False
    return check


primes = make_primes(1_000_000)
for t in range(1, test_cases + 1):
    D, A, B = map(int, input().strip().split())

    result = 0
    for i in range(A, B + 1):
        if primes[i] and str(D) in str(i):
            result += 1
    print('#{} {}'.format(t, result))
