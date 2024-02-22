from string import punctuation


with open("text.txt") as text_file:
    text = text_file.read().split('\n')

with open("output.txt", "w") as output_file:
    for line_index in range(len(text)):
        line = text[line_index]

        letters_count = len([x for x in line if x.isalpha()])
        punctuation_count = len([x for x in line if x in punctuation])

        output_file.write(f"Line {line_index + 1}: {line} ({letters_count})({punctuation_count})\n")

