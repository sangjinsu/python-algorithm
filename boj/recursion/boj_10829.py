import sys

n = int(sys.stdin.readline().strip())


def change_integer_to_binary(num):
    if num <= 1:
        return '1'
    else:
        return change_integer_to_binary(num // 2) + str(num % 2)


sys.stdout.write(change_integer_to_binary(n))
