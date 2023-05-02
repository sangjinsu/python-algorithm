import sys
from collections import deque


def solve(n: int):
    cards = deque([i for i in range(n, 0, -1)])
    while len(cards) > 1:
        cards.pop()
        cards.appendleft(cards.pop())
    sys.stdout.write(str(cards[0]))


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    solve(n)
