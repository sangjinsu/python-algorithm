n = int(input().strip())

for i in range(1, n + 1):
    cnt = 0
    for j in list(str(i)):
        if j in ['3', '6', '9']:
            cnt += 1
    if cnt > 0:
        print('-' * cnt, end=' ')
    else:
        print(i, end=' ')
