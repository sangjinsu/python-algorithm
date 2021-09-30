# 1일차 - 이진수
test_cases = int(input())


# 10진수 -> 2진수
def dec_to_bin(dec):
    binary = ''
    for i in range(3, -1, -1):
        if dec & (1 << i):
            binary += '1'
        else:
            binary += '0'
    return binary


# 16진수 -> 2진수
def hexa_to_bin(hexa):
    binary = ''
    for h in hexa:
        if '0' <= h <= '9':
            binary += dec_to_bin(int(h))
        else:
            num = ord(h) - ord('A') + 10
            binary += dec_to_bin(num)
    return binary


for t in range(1, test_cases + 1):
    N, hexadecimal = input().split()
    result = hexa_to_bin(hexadecimal)
    print('#{} {}'.format(t, result))
