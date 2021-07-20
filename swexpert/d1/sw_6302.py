nums = [12, 24, 35, 70, 88, 120, 155]
result = [n for i, n in enumerate(nums) if i not in [0, 4, 5]]
print(result)