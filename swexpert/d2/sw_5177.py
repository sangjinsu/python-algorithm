# 이진 힙
test_cases = int(input())

for t in range(1, test_cases + 1):
    n = int(input())
    nums = list(map(int, input().split()))
    heap = [0]
    for num in nums:
        heap.append(num)
        idx = len(heap) - 1
        parent = idx // 2
        while parent > 0:
            if heap[idx] < heap[parent]:
                heap[idx], heap[parent] = heap[parent], heap[idx]
            idx = parent
            parent = idx // 2

    result = 0
    parent = (len(heap) - 1) // 2
    while parent > 0:
        result += heap[parent]
        parent = parent // 2

    print('#{} {}'.format(t, result))
