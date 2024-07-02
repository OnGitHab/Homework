from inspect import isgenerator


def generate_cube_numbers(num):
    if num < 10:
        result = None
    else:
        n = 2
        while n ** 3 <= num:
            result = n ** 3
            n += 1
            yield result

    return result


gen = generate_cube_numbers(1)

assert isgenerator(gen) == True
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
print("OK")

