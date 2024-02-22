size = int(input())
matrix = [size * [0] for _ in range(size)]

bombs_count = int(input())


for _ in range(bombs_count):
    bombs = [x for x in input() if x.isdigit()]
    bomb_row, bomb_col = int(bombs[0]), int(bombs[1])
    matrix[bomb_row][bomb_col] = "*"


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1)
}

for row in range(size):
    for col in range(size):
        symbol = matrix[row][col]

        if symbol == "*":
            continue
        else:
            bombs = 0

            for direction in directions:
                next_row, next_col = row + directions[direction][0], col + directions[direction][1]

                if next_row in range(size) and next_col in range(size) and matrix[next_row][next_col] == "*":
                    bombs += 1

        matrix[row][col] = str(bombs)

[print(*element) for element in matrix]