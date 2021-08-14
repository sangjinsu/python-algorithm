def make_skip_table(s: str) -> dict[str]:
    d = dict()
    for i in range(len(s)):
        d[s[i]] = len(s) - i - 1
    print(d)
    return d


def get_skip(d: dict, c: int, p: str) -> int:
    return d.get(c, len(p))


def boyer_moore(pattern: str, s):
    end = len(pattern) - 1
    skip_table = make_skip_table(pattern)
    while end < len(s):
        if pattern[-1] == s[end]:
            found = True
            j = -1
            for i in range(end, end - len(pattern), -1):
                if pattern[j] != s[i]:
                    found = False
                    break
                j -= 1
            if found:
                print(end - len(pattern) + 1)
            end += 1
        else:
            skip = get_skip(skip_table, s[end], pattern)
            end += skip


boyer_moore('mat', 'a parttern matching algorithm')
