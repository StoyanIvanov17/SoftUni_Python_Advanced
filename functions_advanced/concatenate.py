def concatenate(*args, **kwargs):
    string_concatenation = "".join(args)

    for key, value in kwargs.items():
        string_concatenation = string_concatenation.replace(key, value)

    return string_concatenation


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
