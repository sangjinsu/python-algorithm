import sys

num1 = 0b1110
num2 = 0b0101

print(num1 & num2)  # 4
print(num1 | num2)  # 15
print(num1 ^ num2)  # 11
print()

lst = '0000000111100000011000000111100110000110000111100111100111111001100111'


def binary_to_decimal(binary: str):
    num = 0
    i = 1
    for j in range(6, -1, -1):
        num += int(binary[j]) * i
        i <<= 1

    print(str(num))


for i in range(0, len(lst), 7):
    binary = lst[i:i + 7]
    binary_to_decimal(binary)

print()
print(sys.byteorder)


def prtBin(num: int):
    binary = ''
    for i in range(6, -1, -1):
        if num & (1 << i):
            binary += '1'
        else:
            binary += '0'
    return binary


def hexToBin(hexV):
    if '0' <= hexV <= '9':
        return prtBin(int(hexV))
    else:
        return prtBin(ord(hexV) - ord('A') + 10)


lst = '0F97A3'
binary = ''
for i in lst:
    binary += hexToBin(i)

print(binary)
for i in range(0, len(binary), 7):
    b = binary[i:i + 7]
    binary_to_decimal(b)
