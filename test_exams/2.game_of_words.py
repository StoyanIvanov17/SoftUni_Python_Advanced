string = list(input())
size = int(input())

field = []
current_row, current_col = 0, 0

for row in range(size):
    field.append(list(input()))

    if "P" in field[row]:
        current_row, current_col = row, field[row].index("P")

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for _ in range(int(input())):
    command = input()

    next_row, next_col = current_row + directions[command][0], current_col + directions[command][1]

    if not (0 <= next_row < size and 0 <= next_col < size):
        if string:
            string.pop()
        continue

    field[current_row][current_col] = "-"
    position = field[next_row][next_col]

    if position.isalpha():
        string.append(position)

    current_row, current_col = next_row, next_col
    field[current_row][current_col] = "P"

print(f"{''.join(string)}")
for row in field:
    print(f"{''.join(row)}")