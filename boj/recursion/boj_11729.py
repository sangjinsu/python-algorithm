import sys

n = int(sys.stdin.readline().strip())


def hanoi(num, start, to, via):

    def move(start, to):
        print(f'{start} {to}')

    if num == 1:
        move(start, to)
    else:
        hanoi(num - 1, start, via, to)
        move(start, to)
        hanoi(num - 1, via, to, start)


print(2 ** n - 1)
hanoi(n, 1, 3, 2)
