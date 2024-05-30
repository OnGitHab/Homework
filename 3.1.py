

while True:
    a = float(input("..."))1
    action = input("+, -, *, / ")
    b = float(input("..."))
    result = 0
    if action == "+":
        result = a + b
    elif action == "-":
        result = a - b
    elif action == "*":
        result = a * b
    elif action == "/" and  b == 0.0:
        print("you have entered 0 as the second number, cannot perform a division operation with the number  ")
    elif action == "/":
        result = a / b
    else:
        print(f"you chose a invalid symbol for operation!\nPleas select a character from the list")

    print(result)
    break
