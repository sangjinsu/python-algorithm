from itertools import combinations_with_replacement as combr


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


primes = make_primes(1000)
test_cases = int(input())
for t in range(1, test_cases + 1):
    N = int(input().strip())
    combs = list(filter(lambda com: sum(com) == N, combr(primes, 3)))
    print('#{} {}'.format(t, len(combs)))
