nums = [0, 1, 2, 3]

nums_1 = [num for num in nums if num != 0]
nums_2 = [num for num in nums if num == 0]

nums_1.extend(nums_2)

print(nums_1)








