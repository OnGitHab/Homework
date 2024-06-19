import string

st_nm = "1234567890"
st_st = string.punctuation.replace("_", " ")
lst_kw = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield', "get"]

user_input = input("...:\n")

if user_input in lst_kw:
    value = "False"
elif user_input[0] in st_nm:
    value = "False"
elif any(char.isupper() for char in user_input):
    value = "False"
elif any(char in st_st for char in user_input):
    value = "False"
else:
    value = "True"


print(value)


