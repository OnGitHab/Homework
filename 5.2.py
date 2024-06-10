user_input = "yes"

while user_input == "yes":
    a = float(input("First number: "))
    action = input("Choose mathematical operators +, -, *, / ")
    b = float(input("Second number"))
    result = 0
    if action == "+":
        result = a + b
    elif action == "-":
        result = a - b
    elif action == "*":
        result = a * b
    elif action == "/" and b == 0.0:
        print("you have entered 0 as the second number, cannot perform a division operation with the number")
    elif action == "/":
        result = a / b
    else:
        print(f"you chose a invalid symbol for operation!\nPleas select a character from the list")

    print(result)
    user_input = input("if you want to restart print -> 'yes'\n")