
def find_unique_value(lst):
    unique_el = [el for el in lst if lst.count(el) == 1]

    return unique_el[0]


assert find_unique_value([1, 2, 1, 1]) == 2
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5

print("OK")
