def solution(clothes):
    answer = 1
    wear = dict()
    for clothe in clothes:
        wear.setdefault(clothe[1], 0)
        wear[clothe[1]] += 1
    for v in wear.values():
        answer *= v + 1
    answer -= 1
    return answer
