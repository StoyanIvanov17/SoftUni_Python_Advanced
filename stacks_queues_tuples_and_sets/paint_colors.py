from collections import deque

color_segments = deque(input().split())

colors = {"red", "yellow", "blue", "purple", "orange", "green"}
requested_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

result = []

while color_segments:
    first_word = color_segments.popleft()
    second_word = color_segments.pop() if color_segments else ''

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]):
            if el:
                color_segments.insert(len(color_segments) // 2, el)

for color in set(requested_colors.keys()).intersection(result):
    if not requested_colors[color].issubset(result):
        result.remove(color)

print(result)