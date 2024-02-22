def words_sorting(*args):
    ascii_dictionary = {word: sum(map(ord, word)) for word in args}

    if sum(ascii_dictionary.values()) % 2 == 0:
        ascii_dictionary = sorted(ascii_dictionary.items(), key=lambda x: x[0])
    else:
        ascii_dictionary = sorted(ascii_dictionary.items(), key=lambda x: [-x[1]])

    result = ""

    for key, value in ascii_dictionary:
        result += f"{key} - {value}\n"

    return result


