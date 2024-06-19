def second_index(text, some_str):
    if text.count(some_str) < 2:
        x = None
    else:
        x = text.index(some_str)
        x = text.index(some_str, x + 1)
    return x


assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("Hello, hello", "lo") == 10
assert second_index("hi", "h") is None

print("OK")
