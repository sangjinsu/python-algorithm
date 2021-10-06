lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
visited = [False] * 9


def recursion(cnt, value):
    if cnt == 9:
        if value == 10:
            for i in range(len(visited)):
                if visited[i]:
                    print(lst[i], end=' ')
            print()
        return

    if value > 10:
        return

    visited[cnt] = True
    recursion(cnt + 1,  value + lst[cnt])
    visited[cnt] = False
    recursion(cnt + 1, value)


recursion(0, 0)
