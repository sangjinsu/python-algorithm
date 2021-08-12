from sys import stdout, stdin


def octal_to_binary(o):
    octal = int(o)
    if octal == 0:
        return '0'
    result = ''
    while octal != 0:
        octal, result = octal // 2, str(octal % 2) + result
    return result


result = ''
octal = stdin.readline().strip()
for i in range(len(octal)):
    b = octal_to_binary(octal[i])
    result += '0' * (3 - len(b)) + b if i > 0 else b

stdout.write(result)
