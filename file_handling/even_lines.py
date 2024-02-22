def symbols(string):
    for symbol in special_symbols:
        string = string.replace(symbol, "@")

    reversed_string = string.split()
    reversed_string.reverse()

    return " ".join(reversed_string)


special_symbols = ["-", ",", ".", "!", "?"]

with open("text.txt") as file:
    text = file.readlines()

for line in range(0, len(text), 2):
    sentence = text[line]
    print(symbols(sentence))

