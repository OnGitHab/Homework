nums = [1]
print(len(nums))

if len(nums) > 1:
    nums = [[], []]
elif len(nums) == 0:
    list.append([])
elif (len(nums) % 2) == 0:
    sl = int(len(nums)/2)
    list_1 = nums[sl:]
    list_2 = nums[:sl]
    nums = [list_1, list_2]
else:
    sl = int(len(nums)/2) + 1
    list_1 = nums[:sl]
    list_2 = nums[sl:]
    nums = [list_1, list_2]


print(nums)

