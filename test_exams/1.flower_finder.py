from collections import deque

vowels = deque(input().split())
consonants = deque(input().split())

flowers = {"rose": "rose", "tulip": "tulip", "lotus": "lotus", "daffodil": "daffodil"}
word_found = False

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for word in flowers.keys():
        flowers[word] = flowers[word].replace(vowel, "")
        flowers[word] = flowers[word].replace(consonant, "")

        if flowers[word] == "":
            print(f"Word found: {word}")
            word_found = True
            break

    if word_found:
        break

if not word_found:
    print('Cannot find any word!')
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
