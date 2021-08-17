test_cases = int(input().strip())


def make_skip_table(p: str):
    table = [-1] * 256
    for i in range(len(p) - 1, -1 - 1):
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
            return 1
            # start += lenP - t[ord(s[start + lenP])] if start + lenP < lenS else 1
        else:
            start += max(1, j - t[ord(s[start + j])])


for t in range(1, test_cases + 1):
    p = input()
    s = input()
    table = make_skip_table(p)
    result = boyer_moore(p, s)
    if result:
        print('#{} {}'.format(t, 1))
    else:
        print('#{} {}'.format(t, 0))
