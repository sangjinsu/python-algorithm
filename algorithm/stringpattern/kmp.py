# 접두사 접미사 사용


def make_table(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table


def kmp(pattern, string):
    table = make_table(pattern)
    j = 0
    for i in range(len(string)):
        while j > 0 and string[i] != pattern[j]:
            j = table[j - 1]
        if string[i] == pattern[j]:
            if j == len(pattern) - 1:
                print(i - len(pattern) + 1)
                j = table[j]
            else:
                j += 1


kmp('abcabcabcadab', 'abdaabcabcabcbcabcdabcadfdsbcabce')
