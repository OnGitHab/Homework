import string



def first_word(text):
    word_chars = f"{string.ascii_lowercase}{string.ascii_uppercase}'"
    word_lst = []
    text.lstrip(" .,")
    for char in text:
        if char in word_chars:
            word_lst.append(char)
        elif word_lst:
            break

    return "".join(word_lst)


assert first_word("Hello world") == "Hello"
assert first_word("greetings, friends") == "greetings"
assert first_word("don't touch it") == "don't"
assert first_word(".., and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("Hello.World") == "Hello"

print("OK")