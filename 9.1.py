
def popular_words(text, words):
    t = text.lower().split()
    in_text = [t.count(word) for word in words]
    words_in_text = {words[i]: in_text[i] for i in range(len(words))}

    return words_in_text


assert popular_words("When i was One i Had jast begun When i was Two i was nearly new", ["i", "was", "three", "near"]) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}

print("OK")



