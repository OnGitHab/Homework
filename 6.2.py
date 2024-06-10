num_for_calculation = 60
num_for_day_calculation = 24

user_input = int(input("Enter the number of seconds:\n"))

if user_input > 0:
    minutes = user_input / num_for_calculation
    hours = minutes / num_for_calculation
    days = hours / num_for_day_calculation
    print(f" Day: {int(days)}\n Hour: {int(hours)}\n Minutes: {int(minutes)}")
else:
    print("Entered a wrong value, program cannot calculate with negative or None value !!!")



