def solution(numbers, target):
    answer = 0

    def recursion(cnt, num):
        nonlocal answer
        if cnt == len(numbers):
            if num == target:
                answer += 1
            return
        recursion(cnt + 1, num + numbers[cnt])
        recursion(cnt + 1, num - numbers[cnt])

    recursion(0, 0)

    return answer
