test_cases = int(input())


def divide(n, divisor, exponent):
    if n % divisor == 0:
        exponent += 1
        n /= divisor
    return n, exponent


for i in range(test_cases):
    number = int(input())

    a, b, c, d, e = 0, 0, 0, 0, 0
    while number != 1:
        number, a = divide(number, 2, a)
        number, b = divide(number, 3, b)
        number, c = divide(number, 5, c)
        number, d = divide(number, 7, d)
        number, e = divide(number, 11, e)

    print('#{} {} {} {} {} {}'.format(i + 1, a, b, c, d, e))
