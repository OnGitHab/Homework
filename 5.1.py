import keyword
import string

st_nm = "1234567890"
st_st = string.punctuation.replace("_", " ")
lst_kw = keyword.kwlist

user_input = input("...:\n")


if (user_input[0] in st_nm) == True:
    print("Variable cannot begin with a digit")
elif (user_input.istitle()) == True:
    print("Variable cannot contain capital letters")
elif (user_input in st_st) == True:
    print("Variable cannot contain spaces, and punctuation")
elif (user_input in lst_kw) == True:
        print("Variable cannot be any of the keywords")
else:
    print("Can be variable")



