# 이진탐색
test_cases = int(input())


def inorder(k):
    global cnt
    if k > n:
        return
    inorder(k * 2)
    tree[k] = cnt
    cnt += 1
    inorder(k * 2 + 1)


for t in range(1, test_cases + 1):
    n = int(input())
    tree = [0] * (n + 1)
    cnt = 1
    inorder(1)
    print('#{} {} {}'.format(t, tree[1], tree[n // 2]))
