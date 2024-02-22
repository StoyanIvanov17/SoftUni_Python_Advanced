from math import floor

size = int(input())
matrix = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

my_pos = []
my_paths = []

for row in range(size):
    matrix.append(input().split())

    if "P" in matrix[row]:
        my_pos = [row, matrix[row].index("P")]
        my_paths.append(my_pos)

coins = 0

while coins < 100:
    command = input()

    r, c = my_pos[0] + directions[command][0], my_pos[1] + directions[command][1]

    if r < 0:
        r = size - 1
    elif r >= size:
        r = 0
    elif c < 0:
        c = size - 1
    elif c >= size:
        c = 0

    my_pos = [r, c]
    my_paths.append(my_pos)

    if matrix[r][c].isdigit():
        coins += int(matrix[r][c])
        matrix[r][c] = ""

    elif matrix[r][c] == "X":
        coins = floor(coins // 2)
        break

if coins >= 100:
    print(f"You won! You've collected {floor(coins)} coins.")
else:
    print(f"Game over! You've collected {floor(coins)} coins.")

print('Your path:')
[print(x) for x in my_paths]