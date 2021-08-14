# (1) 정렬, dict 사용
# (1-2) 카운트 정렬, dict 사용
# (2) 정렬, hash 사용
def sort_planet_nums(planet_nums, d):
    nums = planet_nums[:]
    for i in range(len(nums) - 1):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if d[nums[min_idx]] > d[nums[j]]:
                min_idx = j
        nums[min_idx], nums[i] = nums[i], nums[min_idx]
    return nums


def make_hash_table(planet_nums):
    table = []

    for num in planet_nums:
        table.append(get_hash_value(num))
    return table


def get_hash_value(num):
    hash_value = 0
    k = 2 ** (len(num) - 1)
    for c in num:
        hash_value += ord(c) * k
        k //= 2
    return hash_value


def find_index(table, v):
    for i in range(len(table)):
        if v == table[i]:
            return i


test_cases = int(input().strip())
planet_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(1, test_cases + 1):
    input()
    nums = input().strip().split()

    # (1) 정렬, dict
    # d = dict()
    # for i in range(len(planet_num)):
    #     d[planet_num[i]] = i
    # nums.sort(key=lambda x: d[x])
    # nums = sort_planet_nums(nums, d)

    # (1 - 2) 정렬, dict
    d = dict()
    for num in nums:
        d.setdefault(num, 0)
        d[num] += 1

    result = ''
    for pn in planet_num:
        result += (pn + ' ') * d[pn]

    # (2) hash 정렬
    # hash_table = make_hash_table(planet_num)
    # nums.sort(key=lambda x: find_index(hash_table, get_hash_value(x)))

    print('#{}'.format(t))
    # print(' '.join(nums))
    print(result)
