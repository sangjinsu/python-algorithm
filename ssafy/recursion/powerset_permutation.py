a = [20, 31, 78]
t = [0] * 3


def powerset(k):
    if k == 3:
        print(t)
    else:
        t[k] = True
        powerset(k + 1)
        t[k] = False
        powerset(k + 1)


def powerset2(k):
    if k == 3:
        print(t)
        for i in range(3):
            if t[i]:
                print(a[i], end=' ')
        print()
    else:
        t[k] = True
        powerset2(k + 1)
        t[k] = False
        powerset2(k + 1)


def powerset3(k):
    if k == 3:
        for i in range(3):
            if t[i]:
                print(a[i], end=' ')
        print()
    else:
        for i in range(2):
            t[k] = i
            powerset3(k + 1)



# 순열
visited = [False] * 3


def per(k):
    if k == 3:
        for i in t:
            print(a[i], end=' ')
        print()
    else:
        for i in range(3):
            if not visited[i]:
                t[k] = i
                visited[i] = True
                per(k + 1)
                visited[i] = False


per(0)
