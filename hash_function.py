import hashlib


def hash_function(text):
    """
    The simple function that returns some inique integer using ordinal encoding
    index and enumerate is used to avoid hash collisions if sequence will be different but characters the same
    EX."Python campBoot" --> "Python Bootcamp"
    repr method is used instead of str to call exactly needed represantation of value like in 3.14 and "3.14"
    """
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(text), start=1))


def hash_function_hashlib(text):
    """
    This solution that uses hashlib I've totally copy-pasted
    """
    hash_object = hashlib.sha256(b'Hello World')
    hex_dig = hash_object.hexdigest()
    return hex_dig


if __name__ == "__main__":
    s = "Python Bootcamp"
    a = "Python campBoot"
    print(hash_function(s), hash_function(a))
    print(hash_function(3.14), hash_function("3.14"))
    print(repr(s))
    print(s)
    print(hash_function_hashlib(s), hash_function_hashlib(a))
