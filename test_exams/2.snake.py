def burrow():
    for row in range(size):
        for col in range(size):
            current_spot = territory[row][col]
            if current_spot == "B":
                return [row, col]


size = int(input())
territory = []
snake_pos = None

for row in range(size):
    territory.append(list(input()))

    if "S" in territory[row]:
        snake_pos = [row, territory[row].index("S")]


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

food = 0

while True:
    command = input()

    current_row, current_col = snake_pos
    next_row, next_col = current_row + directions[command][0], current_col + directions[command][1]

    if not (0 <= next_row < size and 0 <= next_col < size):
        territory[current_row][current_col] = "."
        print(f'Game over!\nFood eaten: {food}')
        break

    symbol = territory[next_row][next_col]
    territory[current_row][current_col] = "."

    if symbol == "B":
        territory[next_row][next_col] = "."
        next_row, next_col = burrow()

    elif symbol == "*":
        food += 1

    territory[next_row][next_col] = "S"
    snake_pos = next_row, next_col

    if food == 10:
        print(f"You won! You fed the snake.\nFood eaten: {food}")
        break

for row in territory:
    print(f"{''.join(row)}")