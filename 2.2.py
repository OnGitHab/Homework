numbers = int(input("..."))

numbers, a = divmod(numbers, 10)
numbers, b = divmod(numbers, 10)
numbers, c = divmod(numbers, 10)
numbers, d = divmod(numbers, 10)
numbers, f = divmod(numbers, 10)


print( (f + d * 10) + (c * 100) + (b * 1000) + (a * 10000))



