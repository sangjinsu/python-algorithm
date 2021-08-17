def make_skip_table(p: str):
    table = [0] * 256
    for i in range(len(p)):
        table[ord(p[i])] = i
    return table


def boyer_moore(p, s):
    lenP = len(p)
    lenS = len(s)

    t = make_skip_table(p)
    start = 0
    while start <= lenS - lenP:
        j = lenP - 1
        while j >= 0 and p[j] == s[start + j]:
            j -= 1

        if j < 0:
            start += lenP - t[ord(s[start + lenP])] if start + lenP < lenS else 1
        else:
            start += max(1, j - t[ord(s[start + j])])


boyer_moore('abcd', 'abcdeeabcd')
