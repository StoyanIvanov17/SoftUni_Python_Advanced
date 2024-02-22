rows, cols = [int(x) for x in input().split()]
matrix = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}


boy_pos = None
start_row, start_col = None, None

for row in range(rows):
    matrix.append(list(input()))

    if "B" in matrix[row]:
        boy_pos = [row, matrix[row].index("B")]
        start_row, start_col = boy_pos


while True:
    current_row, current_col = boy_pos
    command = input()

    next_row, next_col = current_row + directions[command][0], current_col + directions[command][1]

    if not (0 <= next_row < rows and 0 <= next_col < cols):
        print("The delivery is late. Order is canceled.")
        matrix[start_row][start_col] = " "
        break

    next_spot = matrix[next_row][next_col]

    if next_spot == "*":
        continue

    elif next_spot == "P":
        matrix[next_row][next_col] = "R"
        print('Pizza is collected. 10 minutes for delivery.')

    elif next_spot == "A":
        matrix[next_row][next_col] = "P"
        print('Pizza is delivered on time! Next order...')
        matrix[start_row][start_col] = "B"
        break

    elif next_spot == "-":
        matrix[next_row][next_col] = "."

    current_row, current_col = next_row, next_col
    boy_pos = current_row, current_col

for row in matrix:
    print(f"{''.join(row)}")
