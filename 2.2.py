numbers = int(input("..."))

numbers, a = divmod(numbers, 10)
numbers, b = divmod(numbers, 10)
numbers, c = divmod(numbers, 10)
numbers, d = divmod(numbers, 10)
numbers, f = divmod(numbers, 10)

print(str(a) + str(b) + str(c) + str(d) + str(f))



