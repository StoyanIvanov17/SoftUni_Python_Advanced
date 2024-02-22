rows, cols = [int(x) for x in input().split(', ')]
matrix = []

santa_row, santa_col = None, None
is_it_christmas = False

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

christmas_decorations = 0
gifts = 0
cookies = 0
all_items = 0

for row in range(rows):
    matrix.append(input().split())

    if "Y" in matrix[row]:
        santa_row, santa_col = row, matrix[row].index("Y")

    all_items += matrix[row].count("D")
    all_items += matrix[row].count("G")
    all_items += matrix[row].count("C")

while True:
    info = input().split('-')

    command = info[0]
    if command == "End":
        break

    moves = int(info[1])

    for step in range(moves):
        matrix[santa_row][santa_col] = "x"
        next_row = santa_row + directions[command][0]
        next_col = santa_col + directions[command][1]

        if next_row == rows:
            next_row = 0
        elif next_row == -1:
            next_row = rows - 1

        if next_col == cols:
            next_col = 0
        elif next_col == -1:
            next_col = cols - 1

        if matrix[next_row][next_col] == "D":
            christmas_decorations += 1
        elif matrix[next_row][next_col] == "G":
            gifts += 1
        elif matrix[next_row][next_col] == "C":
            cookies += 1

        santa_row, santa_col = next_row, next_col
        matrix[santa_row][santa_col] = "Y"

        if christmas_decorations + gifts + cookies == all_items:
            print('Merry Christmas!')
            is_it_christmas = True
            break

    if is_it_christmas:
        break


print("You've collected:")
print(f"- {christmas_decorations} Christmas decorations")
print(f"- {gifts} Gifts")
print(f"- {cookies} Cookies")

[print(*line) for line in matrix]