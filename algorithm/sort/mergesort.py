def mergesort(m):
    if len(m) == 1:
        return m

    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result
