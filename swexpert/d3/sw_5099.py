# 피자 굽기
test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n, m = map(int, input().strip().split())

    pizza_lst = list(map(int, input().strip().split()))
    fire_queue = []
    pizza_num = -1

    for i in range(n):
        pizza_num += 1
        fire_queue.append([pizza_num + 1, pizza_lst[pizza_num]])

    while len(fire_queue) > 1:
        pizza = fire_queue.pop(0)
        pizza[1] //= 2
        if pizza[1] > 0:
            fire_queue.append(pizza)
        else:
            if pizza_num < m - 1:
                pizza_num += 1
                fire_queue.append([pizza_num + 1, pizza_lst[pizza_num]])

    result = fire_queue[0][0]
    print('#{} {}'.format(t, result))
