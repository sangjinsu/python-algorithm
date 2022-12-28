import sys
import math


def is_prime(num: int) -> bool:
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    return True


def recursion(num: int, depth: int):
    if depth == N:
        if is_prime(num):
            sys.stdout.write(str(num) + '\n')
            return

    if is_prime(num):
        for i in range(1, 10):
            recursion(int(str(num) + str(i)), depth + 1)


N = int(sys.stdin.readline().strip())
for i in [2, 3, 5, 7]:
    recursion(i, 1)
