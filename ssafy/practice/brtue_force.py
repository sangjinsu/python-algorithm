def bruteforce(s, p):
    sLen = len(s)
    pLen = len(p)
    i = 0
    j = -1
    while i < sLen and j < pLen:
        if s[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == pLen:
            print(i - pLen)
            j = -1
            i = i - j


bruteforce('the is book is mine', 'is')