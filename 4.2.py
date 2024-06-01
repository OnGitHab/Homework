nums = [0, 1, 2, 3, 4, 5, 6]
nums_1 = []
i = 0

for num in nums:
    if nums[i] % 2 == 0:
        nums_1.append(nums[i] * nums[-1])
        i = i + 1
    else:
        i = i + 1


for i in nums_1:
    i = i + i

print(nums_1)
print(i)


