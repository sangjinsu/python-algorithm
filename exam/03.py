def solution(stones, k):
    answer = '-1'

    if min(stones) + max(stones) < k:
        return answer

    def recursion(value):
        nonlocal answer

        if stones.count(k) == 1 and stones.count(0) == len(stones) - 1:
            answer = value
            return

        for i in range(len(stones)):
            stones[i] += 2
            for j in range(len(stones)):
                stones[j] -= 1

            if not stones.count(-1):
                recursion(value + str(i))

            stones[i] -= 2
            for j in range(len(stones)):
                stones[j] += 1

    recursion('')

    return answer


print(solution([5, 7, 2, 4, 9], 20))
