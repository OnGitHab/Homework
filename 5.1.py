import string

st_nm = "1234567890"
st_st = string.punctuation.replace("_", " ")
lst_kw = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield', "get"]

user_input = input("...:\n")


if user_input[0] in st_nm:
    print("False")
elif user_input:
    print(user_input.istitle())
elif user_input in st_st or "__" in user_input:
    print("False")
elif len(user_input) > 0:
    for el in lst_kw:
        common_chars = set(user_input) & set(el)
        similarity = len(common_chars) / max(len(set(user_input)), len(set(el)))
        if similarity == 1:
            print("False")
else:
    print("True")

