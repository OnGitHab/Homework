def add_one(lst_num):
    lst_str_num = [str(num) for num in lst_num]
    str_num = "".join(lst_str_num)
    str_num = str(int(str_num) + 1)
    lst_num = [int(el) for el in str_num]
    return lst_num


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5]
assert add_one([9, 9, 9]) == [1, 0, 0, 0]
assert add_one([0]) == [1]
assert add_one([9]) == [1, 0]

print("OK")
