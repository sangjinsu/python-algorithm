def solution(lottos, win_nums):
    score = [6, 6, 5, 4, 3, 2, 1]

    cnt_zero = 0
    matched = 0

    for lotto in lottos:
        if lotto == 0:
            cnt_zero += 1
        if lotto in win_nums:
            matched += 1

    result = [score[matched + cnt_zero], score[matched]]
    return result
