from inspect import isgenerator


def prime_generator(num):
    if num < 2:
        n = None
    else:
        n = 2
        yield n
        n = 1
        for _ in range(3):
            n = n + 2
            yield n
        while n + 2 <= num:
            n = n + 2
            if divmod(n, 3)[1] != 0 and divmod(n, 5)[1] != 0 and divmod(n, 7)[1] != 0:
                yield n

    return n


gen = prime_generator(1)

assert isgenerator(gen) == True
assert list(prime_generator(10)) == [2, 3, 5, 7]
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13]
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print("OK")