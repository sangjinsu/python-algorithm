def solution(phone_book):
    answer = True
    phone_nums = dict()
    for number in phone_book:
        phone_nums[number] = True

    for number in phone_book:
        for i in range(len(number)):
            if phone_nums.get(number[:i], False):
                answer = False

    return answer
