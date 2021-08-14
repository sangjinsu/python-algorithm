def make_skip_table(s: str) -> dict[str]:
    d = dict()
    for i in range(len(s)):
        d[s[i]] = len(s) - i - 1
    print(d)
    return d


def boyer_moore(p: str, s):
    lenP = len(p)
    lenS = len(s)

    t = make_skip_table(p)

    start = 0
    while start <= lenS - lenP:
        j = lenP - 1

        while j >= 0 and p[j] == s[start + j]:
            j -= 1

        if j == -1:
            print(start)
            start += lenP - t.get(s[start + lenP]) if start + lenP < lenS else 1
        else:
            start += max(1, t.get(s[start + j], lenP + 1))



boyer_moore('rithm', 'a pattern matching algorithm')
