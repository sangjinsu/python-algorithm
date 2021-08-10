test_cases = int(input().strip())


def is_most_and_highest_numbered_card(max_count, count, max_num, num):
    return max_count < count or (max_count == count and max_num < num)


for t in range(1, test_cases + 1):
    n = int(input().strip())
    nums = list(map(int, list(input().strip())))

    max_num = -1
    for num in nums:
        if max_num < num:
            max_num = num

    counts = [0] * (max_num + 1)

    for num in nums:
        counts[num] += 1

    max_count = -1
    num = -1
    for i in range(len(counts)):
        if is_most_and_highest_numbered_card(max_count, counts[i], num, i):
            max_count = counts[i]
            num = i

    print('#{} {} {}'.format(t, num, max_count))
