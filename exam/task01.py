def solution(S, K):
    # write your code in Python 3.6
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    remain = K % 7
    idx = (days.index(S) + remain) % 7
    return days[idx]
