test_cases = 10


def inorder(n):
    if n != 0:
        inorder(tree[n][0])
        print(data.get(n), end='')
        inorder(tree[n][1])


for t in range(1, test_cases + 1):
    v = int(input().strip())
    tree = [[0] * 2 for _ in range(v + 1)]
    data = dict()
    for i in range(1, v + 1):
        line = input().strip().split()
        node, value, *argv = line
        node = int(node)
        if len(argv) == 2:
            tree[node][0] = int(argv[0])
            tree[node][1] = int(argv[1])
        elif len(argv) == 1:
            tree[node][0] = int(argv[0])
        data[node] = value

    print('#{}'.format(t), end=' ')
    inorder(1)
    print()
