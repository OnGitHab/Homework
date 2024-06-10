nums = input("Enter the number")
i = 0
result = 11

while result > 9:
    num_multi = 1
    for i in range(len(nums)):
        num = nums[i]
        i += 1
        num_multi *= int(num)

    nums = str(num_multi)
    result = num_multi

print(result)





