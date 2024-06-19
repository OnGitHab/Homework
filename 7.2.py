def correct_sentence(text):
    if "." in text:
        x = text.index(".")
        text_cut = text[:x + 2].capitalize()
        text_cut_1 = text[x + 2:].capitalize()
        text = f"{text_cut}{text_cut_1}"
    else:
        text = text.capitalize()
    if not text.endswith("."):
        text += "."

    return text


assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("hello") == "Hello."
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
print("OK")