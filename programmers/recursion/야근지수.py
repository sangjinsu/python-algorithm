import heapq


def solution(n, works):
    for i in range(len(works)):
        works[i] *= -1

    heapq.heapify(works)

    for i in range(n):
        work = heapq.heappop(works)
        if work == 0:
            heapq.heappush(works, work)
            break
        work += 1
        heapq.heappush(works, work)

    answer = sum(map(lambda x: x ** 2, list(works)))
    return answer


n = 4
works = [4, 3, 3]
print(solution(n, works))
