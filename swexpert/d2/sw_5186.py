# 1일차 - 이진수2
test_cases = int(input())


# 10진수 -> 2진수
def dec_to_bin(decimal):
    binary = ''
    while decimal != 0:
        decimal *= 2
        if decimal >= 1:
            decimal -= 1
            binary += '1'
        else:
            binary += '0'

        if len(binary) >= 13:
            binary = 'overflow'
            break

    return binary


for t in range(1, test_cases + 1):
    N = float(input())
    result = dec_to_bin(N)
    print('#{} {}'.format(t, result))
