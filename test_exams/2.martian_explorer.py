from collections import deque


size = 6
matrix = []
martian_row, martian_col = 0, 0

for rows in range(size):
    matrix.append(input().split())

    if "E" in matrix[rows]:
        martian_row, martian_col = rows, matrix[rows].index("E")


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

water_deposit = 0
concrete_deposit = 0
metal_deposit = 0

commands = deque(input().split(', '))
while commands:
    command = commands.popleft()

    row, col = martian_row + directions[command][0], martian_col + directions[command][1]

    if row < 0:
        row = size - 1
    elif row >= size:
        row = 0
    elif col < 0:
        col = size - 1
    elif col >= size:
        col = 0

    martian_row, martian_col = row, col

    if matrix[martian_row][martian_col] == "W":
        water_deposit += 1
        print(f"Water deposit found at ({martian_row}, {martian_col})")
    elif matrix[martian_row][martian_col] == "M":
        metal_deposit += 1
        print(f"Metal deposit found at ({martian_row}, {martian_col})")
    elif matrix[martian_row][martian_col] == "C":
        concrete_deposit += 1
        print(f"Concrete deposit found at ({martian_row}, {martian_col})")
    elif matrix[martian_row][martian_col] == "R":
        print(f"Rover got broken at ({martian_row}, {martian_col})")
        break

if water_deposit > 0 and concrete_deposit > 0 and metal_deposit > 0:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
