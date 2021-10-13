# 정식이의 은행업무

def get_possible_binary(base):
    nums = list()
    for i in range(len(base)):
        temp = base[:]
        if base[i] == '0':
            temp[i] = '1'
            nums.append(''.join(temp))
        else:
            temp[i] = '0'
            nums.append(''.join(temp))
    return nums


def get_possible_ternary(base):
    nums = list()
    for i in range(len(base)):
        temp = base[:]
        if base[i] == '0':
            temp[i] = '1'
            nums.append(''.join(temp))
            temp[i] = '2'
            nums.append(''.join(temp))
        elif base[i] == '1':
            temp[i] = '0'
            nums.append(''.join(temp))
            temp[i] = '2'
            nums.append(''.join(temp))
        elif base[i] == '2':
            temp[i] = '0'
            nums.append(''.join(temp))
            temp[i] = '1'
            nums.append(''.join(temp))
    return nums


def change_to_decimal(number, notation):
    decimal = 0
    m = 1
    for n in reversed(number):
        decimal += int(n) * m
        m *= notation
    return decimal


test_cases = int(input().strip())
for t in range(1, test_cases + 1):
    binary = list(input().strip())
    ternary = list(input().strip())

    binary_list = get_possible_binary(binary)
    ternary_list = get_possible_ternary(ternary)

    binary_set = set(map(lambda base: change_to_decimal(base, 2), binary_list))
    ternary_set = set(map(lambda base: change_to_decimal(base, 3), ternary_list))

    result = binary_set & ternary_set
    print('#{} {}'.format(t, *result))

