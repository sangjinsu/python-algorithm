def my_reverse(s):
    r = list(s)
    left = 0
    right = len(r) - 1

    while left <= right:
        temp = r[left]
        r[left] = r[right]
        r[right] = temp

        left += 1
        right -= 1

    return ''.join(r)


print(my_reverse('abcdefgh'))
