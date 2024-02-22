size = int(input())
battlefield = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

mine_hits = 0
enemy_cruisers = 3

current_row, current_col = None, None

for row in range(size):
    battlefield.append(list(input()))

    if "S" in battlefield[row]:
        current_row, current_col = row, battlefield[row].index("S")


while True:
    if mine_hits == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{current_row}, {current_col}]!")
        break

    if enemy_cruisers == 0:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    command = input()

    next_row, next_col = current_row + directions[command][0], current_col + directions[command][1]

    if battlefield[next_row][next_col] == "-":
        battlefield[current_row][current_col] = "-"
        current_row, current_col = next_row, next_col
        battlefield[current_row][current_col] = "S"

    elif battlefield[next_row][next_col] == "*":
        mine_hits += 1
        battlefield[current_row][current_col] = "-"
        current_row, current_col = next_row, next_col
        battlefield[current_row][current_col] = "S"

    elif battlefield[next_row][next_col] == "C":
        enemy_cruisers -= 1
        battlefield[current_row][current_col] = "-"
        current_row, current_col = next_row, next_col
        battlefield[current_row][current_col] = "S"

for field in battlefield:
    print(f"{''.join(field)}")