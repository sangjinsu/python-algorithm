import sys


def binary_to_octal(binary):
    result = 0
    k = 1
    for i in range(len(binary) - 1, -1, -1):
        result += int(binary[i]) * k
        k *= 2
    return str(result)


binary = sys.stdin.readline().strip()

result = ''
for i in range(len(binary), 0, -3):
    if i < 3:
        result = binary_to_octal(binary[:i]) + result
    else:
        result = binary_to_octal(binary[i - 3: i]) + result

sys.stdout.write(result)
