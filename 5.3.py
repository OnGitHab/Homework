import string

user_input = input("...")

user_input = user_input.translate(str.maketrans("","",string.punctuation))

words = user_input.split()
words = [word.capitalize() for word in words]

hashtag = "#" + "".join(words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]


print(hashtag)







