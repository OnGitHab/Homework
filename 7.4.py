import random


def common_elements():
    lst_multiples_3 = {3 * el for el in range(100)}
    lst_multiples_5 = {5 * el for el in range(100)}
    intersection = lst_multiples_3.intersection(lst_multiples_5)
    return intersection


result = common_elements()
print(result)