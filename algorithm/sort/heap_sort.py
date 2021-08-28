def downheap(i, size):
    while 2 * i <= size:
        k = 2 * i
        if k < size and a[k] < a[k + 1]:
            k += 1
        if a[i] >= a[k]:
            break
        a[i], a[k] = a[k], a[i]
        i = k


def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize // 2 + 1)):
        downheap(i, hsize)


def heap_sort(a):
    N = len(a) - 1
    for i in range(N):
        a[1], a[N] = a[N], a[1]
        downheap(1, N - 1)
        N -= 1


a = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
create_heap(a)
heap_sort(a)
print(a)