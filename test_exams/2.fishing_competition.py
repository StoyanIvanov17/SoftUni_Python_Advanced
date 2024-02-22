size = int(input())
matrix = []

fisher_pos = []
fish_caught = 0
whirlpool = False

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for row in range(size):
    matrix.append(list(input()))

    if "S" in matrix[row]:
        fisher_pos = [row, matrix[row].index("S")]
        matrix[row][fisher_pos[1]] = "-"

while True:
    command = input()
    if command == "collect the nets":
        row = fisher_pos[0]
        col = fisher_pos[1]
        matrix[row][col] = "S"
        break

    r, c = fisher_pos[0] + directions[command][0], fisher_pos[1] + directions[command][1]

    if r < 0:
        r = size - 1
    elif r >= size:
        r = 0
    elif c < 0:
        c = size - 1
    elif c >= size:
        c = 0

    fisher_pos = [r, c]

    if matrix[r][c].isdigit():
        fish_amount = int(matrix[r][c])
        fish_caught += fish_amount
        matrix[r][c] = "-"

    elif matrix[r][c] == "W":
        fish_caught = 0
        whirlpool = True
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the "
              f"ship: [{r},{c}]")
        break


if fish_caught >= 20:
    print("Success! You managed to reach the quota!")
elif not whirlpool:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - fish_caught} tons of fish more.")

if fish_caught > 0:
    print(f"Amount of fish caught: {fish_caught} tons.")

if not whirlpool:
    for row in matrix:
        print(f"{''.join(row)}")