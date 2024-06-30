def is_even(x):
    if bin(x).endswith("0"):
        result = True
    else:
        result = False
    return result


assert is_even(2) == True
assert is_even(5) == False
assert is_even(0) == True
print("OK")