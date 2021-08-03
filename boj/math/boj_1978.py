import sys

n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


cnt = 0
for num in nums:
    if isPrime(num):
        cnt += 1

sys.stdout.write(str(cnt))
