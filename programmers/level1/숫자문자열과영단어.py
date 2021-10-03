def solution(s):
    table = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    result = ''
    temp = ''
    keys = table.keys()
    for letter in s:
        if '0' <= letter <= '9':
            result += letter
        else:
            temp += letter
            if temp in keys:
                result += table.get(temp)
                temp = ''

    return int(result)
