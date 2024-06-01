import random

nums = []
lst_nums = []

for num in range(random.randint(3,10)):
    num = random.randint(1,10)
    lst_nums.append(num)

print(lst_nums)

nums = [lst_nums[0], lst_nums[2], lst_nums[-2]]

print(nums)






