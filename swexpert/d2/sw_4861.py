test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n, m = tuple(map(int, input().strip().split()))
    strings = [input().strip() for _ in range(n)]
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
                print('#{} {}'.format(t, strings[i][j:j + m]))

            while c_top <= c_bot:
                if strings[c_top][i] != strings[c_bot][i]:
                    break
                c_top += 1
                c_bot -= 1
            if c_top > c_bot:
                print('#{} {}'.format(t, ''.join([strings[k][i] for k in range(j, j + m)])))
