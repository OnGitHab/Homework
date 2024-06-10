import string

st_range = string.ascii_lowercase + string.ascii_uppercase

user_input = input("Write two symbols separate by '-':\n")
letter_1 = user_input[0]
letter_2 = user_input[2]

if letter_1 in st_range and letter_2 in st_range:
    letter_1_index = st_range.index(letter_1)
    letter_2_index = st_range.index(letter_2)
    print(st_range[letter_1_index:letter_2_index+1])
else:
    print("...")




