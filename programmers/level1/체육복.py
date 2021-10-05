def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    for res in reserve_set:
        if res - 1 in lost_set:
            lost_set.remove(res - 1)
        elif res + 1 in lost_set:
            lost_set.remove(res + 1)
    result = n - len(lost_set)
    return result
