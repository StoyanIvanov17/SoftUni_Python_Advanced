matrix = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for _ in range(6):
    matrix.append(input().split())

row, col = [int(x) for x in list(input()) if x.isdigit()]

while True:
    command = input().split(', ')
    if command[0] == "Stop":
        break

    row, col = row + directions[command[1]][0], col + directions[command[1]][1]

    if command[0] == "Create":
        if matrix[row][col] == ".":
            matrix[row][col] = command[2]

    elif command[0] == "Update":
        if matrix[row][col] != ".":
            matrix[row][col] = command[2]

    elif command[0] == "Delete":
        if matrix[row][col] != ".":
            matrix[row][col] = "."

    elif command[0] == "Read":
        if matrix[row][col] != ".":
            print(f"{matrix[row][col]}")

for m in matrix:
    print(f"{' '.join(m)}")
