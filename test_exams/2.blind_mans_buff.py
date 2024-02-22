rows, cols = map(int, input().split())
playground = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

touched = 0
moves = 0
current_row, current_col = None, None

for row in range(rows):
    playground.append(input().split())

    if "B" in playground[row]:
        current_row, current_col = row, playground[row].index("B")


while touched < 3:
    command = input()
    if command == 'Finish':
        break

    next_row, next_col = current_row + directions[command][0], current_col + directions[command][1]

    if not (0 <= next_row < rows and 0 <= next_col < cols):
        continue

    if playground[next_row][next_col] == "O":
        continue

    if playground[next_row][next_col] == "P":
        moves += 1
        touched += 1
        playground[current_row][current_col] = "-"
        current_row, current_col = next_row, next_col
        playground[current_row][current_col] = "B"

    if playground[next_row][next_col] == "-":
        moves += 1
        playground[current_row][current_col] = "-"
        current_row, current_col = next_row, next_col
        playground[current_row][current_col] = "B"

print(f"Game over!\nTouched opponents: {touched} Moves made: {moves}")