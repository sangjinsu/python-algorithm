def solution(array, commands):
    result = []
    for command in commands:
        i, j, k = command
        result.append(sorted(array[i - 1:j])[k - 1])
    return result
