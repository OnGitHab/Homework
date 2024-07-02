def is_iven(number):
    if bin(number).endswith("1"):
        return False
    else:
        return True


assert is_iven(2494563894038 ** 2) == True
assert is_iven(1056897 ** 2) == False
assert is_iven(24945638940387 ** 3) == False
print("OK")
