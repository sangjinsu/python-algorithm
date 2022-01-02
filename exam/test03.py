# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(D, X):
    # write your code in Python 3.6
    idx = len(D) - 1
    cnt = 0
    diff = 0
    while idx >= 0:
        diff += abs(D[idx] - D[idx - 1])
        if diff == X:
            diff = 0
            cnt += 1
            idx -= 1
        elif diff > X:
            diff = 0
            cnt += 1
        idx -= 1

    if diff > 0:
        cnt += 1

    return cnt


solution([5, 8, 2, 7], 3)
