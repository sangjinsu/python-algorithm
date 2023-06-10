import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    cards = list(map(int, sys.stdin.readline().strip().split()))
    M = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))

    indices = {}
    for i in range(N):
        indices[cards[i]] = 1

    for num in nums:
        if indices.get(num):
            sys.stdout.write(str(1) + ' ')
        else:
            sys.stdout.write(str(0) + ' ')
