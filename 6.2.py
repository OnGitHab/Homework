user_input = input("")


if int(user_input) < 8640000:
    minutes, seconds_print = divmod(int(user_input), 60)
    hours, minutes_print = divmod(minutes, 60)
    days, hours_print = divmod(hours, 24)

    if "2" in str(days):
        days_word = "дні"
    elif days > 20 and str(days)[-1] == "1":
        days_word = "день"
    else:
        days_word = "днів"

    values_print = [str() ]

values_print = [str(hours_print), str(minutes_print), str(seconds_print)]
values_print = [f"0{el}" if len(el) <= 1 else el for el in values_print]

print(f"{days} {days_word}, {values_print[0]}:{values_print[1]}:{values_print[2]}")