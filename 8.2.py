import string


def is_palindrome(st):
    st_for_check = string.punctuation + string.whitespace
    st_clean = "".join([el for el in st if el not in st_for_check])

    return st_clean.lower() == st_clean[::-1].lower()


assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("OP") is False
assert is_palindrome("a.") is True
assert is_palindrome("aurora") is False

print("OK")