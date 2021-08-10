test_cases = int(input().strip())

for t in range(1, test_cases + 1):
    n, m = tuple(map(int, input().strip().split()))
    nums = list(map(int, input().strip().split()))
    start = 0
    end = m

    slide = 0
    for i in range(m):
        slide += nums[i]

    min_slide, max_slide = slide, slide

    for i in range(1, n - m + 1):

        slide = slide - nums[start] + nums[end]
        if min_slide > slide:
            min_slide = slide

        if max_slide < slide:
            max_slide = slide

        start += 1
        end += 1

    result = max_slide - min_slide
    print('#{} {}'.format(t, result))
