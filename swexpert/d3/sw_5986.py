def make_primes(n):
    k = n + 1
    check = [True] * k
    check[0] = False
    check[1] = False
    m = int(k ** 0.5)
    for i in range(2, m + 1):
        if check[i]:
            for j in range(i + i, k, i):
                check[j] = False
    return [num for num in range(k) if check[num]]


test_cases = int(input())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    primes = make_primes(N)
    result = 0
    for i in range(len(primes) // 2):
        for j in range(i, len(primes)):
            if primes[i] + primes[j] > N:
                break
            if N - (primes[i] + primes[j]) in primes[j:]:
                result += 1

    print('#{} {}'.format(t, result))
