test_cases = 10


def search_palindromes(strings, n, m):
    for i in range(n):
        for j in range(n - m + 1):
            r_left = j
            r_right = j + m - 1

            c_top = j
            c_bot = j + m - 1

            while r_left <= r_right:
                if strings[i][r_left] != strings[i][r_right]:
                    break
                r_left += 1
                r_right -= 1
            if r_left > r_right:
                return m

            while c_top <= c_bot:
                if strings[c_top][i] != strings[c_bot][i]:
                    break
                c_top += 1
                c_bot -= 1
            if c_top > c_bot:
                return m
    return -1


for t in range(1, test_cases + 1):
    test_num = int(input())
    n = 100
    strings = [input().strip() for _ in range(n)]

    max_len = 0
    for m in range(1, n):
        result = search_palindromes(strings, n, m)
        max_len = result if result > max_len else max_len

    print('#{} {}'.format(t, max_len))