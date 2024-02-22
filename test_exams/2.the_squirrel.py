size = int(input())
matrix = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

hazelnuts = 0
squirrel_pos = []
ops = False

commands = list(input().split(', '))
for row in range(size):
    matrix.append(list(input()))

    if "s" in matrix[row]:
        squirrel_pos = [row, matrix[row].index("s")]

for command in commands:
    next_row, next_col = squirrel_pos[0] + directions[command][0], squirrel_pos[1] + directions[command][1]

    if not (0 <= next_row < size and 0 <= next_col < size):
        print('The squirrel is out of the field.')
        ops = True
        break

    squirrel_pos = [next_row, next_col]

    if matrix[next_row][next_col] == "h":
        hazelnuts += 1
        matrix[next_row][next_col] = "*"
        if hazelnuts == 3:
            print('Good job! You have collected all hazelnuts!')
            break

    if matrix[next_row][next_col] == "*":
        continue

    if matrix[next_row][next_col] == "t":
        print('Unfortunately, the squirrel stepped on a trap...')
        ops = True
        break

if not ops and hazelnuts < 3:
    print('There are more hazelnuts to collect.')

print(f"Hazelnuts collected: {hazelnuts}")