size = int(input())

game_amount = 100
matrix = []
gambler_pos = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

for row in range(size):
    matrix.append(list(input()))

    if "G" in matrix[row]:
        gambler_pos = [row, matrix[row].index("G")]
        matrix[row][gambler_pos[1]] = "-"

while True:
    command = input()

    if command == 'end':
        print(f"End of the game. Total amount: {game_amount}$")
        matrix[gambler_pos[0]][gambler_pos[1]] = 'G'

        for row in matrix:
            print(f"{''.join(row)}")
        break

    r, c = gambler_pos[0] + directions[command][0], gambler_pos[1] + directions[command][1]

    if not (0 <= r < size and 0 <= c < size):
        continue

    gambler_pos = [r, c]

    if matrix[r][c] == "W":
        game_amount += 100
        matrix[r][c] = "-"

    elif matrix[r][c] == "P":
        game_amount -= 200

        if game_amount <= 0:
            print("Game over! You lost everything!")
            break

        else:
            matrix[r][c] = "-"

    elif matrix[r][c] == "J":
        game_amount += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {game_amount}$")
        matrix[r][c] = 'G'

        for row in matrix:
            print(f"{''.join(row)}")
        break
