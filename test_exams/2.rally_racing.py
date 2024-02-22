size = int(input())
racing_number = input()

matrix = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

kilometers_covered = 0
car_row, car_col = 0, 0

for row in range(size):
    matrix.append(input().split())


def other_side_of_tunnel(mat):
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if mat[r][c] == "T":
                return r, c


while True:
    command = input()
    if command == "End":
        matrix[car_row][car_col] = "C"
        print(f"Racing car {racing_number} DNF.")
        break

    next_row, next_col = car_row + directions[command][0], car_col + directions[command][1]

    if matrix[next_row][next_col] == ".":
        kilometers_covered += 10
        matrix[car_row][car_col] = "."
        car_row, car_col = next_row, next_col
        matrix[car_row][car_col] = "C"

    elif matrix[next_row][next_col] == "T":
        kilometers_covered += 30
        matrix[car_row][car_col] = "."
        matrix[next_row][next_col] = "."
        car_row, car_col = other_side_of_tunnel(matrix)
        matrix[car_row][car_col] = "."

    elif matrix[next_row][next_col] == "F":
        kilometers_covered += 10
        matrix[car_row][car_col] = "."
        car_row, car_col = next_row, next_col
        matrix[car_row][car_col] = "C"
        print(f"Racing car {racing_number} finished the stage!")
        break

print(f"Distance covered {kilometers_covered} km.")
for row in matrix:
    print(f"{''.join(row)}")