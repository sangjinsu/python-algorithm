import sys

primes = [True] * (1000000 + 1)
primes[0] = False
primes[1] = False

m = int(1000000 ** 0.5)
for i in range(2, m + 1):
    if primes[i]:
        for j in range(i * 2, 1000000 + 1, i):
            primes[j] = False

while True:
    num = int(sys.stdin.readline().strip())
    if num == 0:
        break

    for i in range(3, 1000000 + 1):
        if primes[i] and primes[num - i]:
            sys.stdout.write(f'{num} = {i} + {num - i}\n')
            break
    else:
        sys.stdout.write("Goldbach's conjecture is wrong.")
