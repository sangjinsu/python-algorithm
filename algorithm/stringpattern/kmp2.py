def make_table(p: str) -> list[int]:
    lenP = len(p)
    table = [0] * lenP
    j = 0
    i = 1
    while i < lenP:
        if p[i] == p[j]:
            j += 1
            table[i] = j
            i += 1
        else:
            if j > 0:
                j = table[j - 1]
            else:
                i += 1
    return table


def kmp(p: str, s: str):
    table = make_table(p)
    j = 0
    i = 0
    lenS = len(s)
    lenP = len(p)
    while i < len(s):
        if s[i] == p[j]:
            if j == lenP - 1:
                print(i - lenP + 1)
                j = table[j]
            else:
                j += 1
            i += 1
        else:
            if j > 0:
                j = table[j - 1]
            else:
                i += 1


kmp('abacaba', 'absdedabacaba')
