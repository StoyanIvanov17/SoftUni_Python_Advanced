size = int(input())
airspace = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

jet_pos = None, None
enemy_fighters = 4

for row in range(size):
    airspace.append(list(input()))

    if "J" in airspace[row]:
        jet_pos = [row, airspace[row].index("J")]


armor = 300

while True:
    current_row, current_col = jet_pos
    command = input()

    next_row, next_col = current_row + directions[command][0], current_col + directions[command][1]
    symbol = airspace[next_row][next_col]

    if symbol == "-":
        jet_pos = next_row, next_col
        airspace[current_row][current_col] = "-"
        continue

    elif symbol == "E":
        enemy_fighters -= 1
        airspace[current_row][current_col] = "-"

        if enemy_fighters == 0:
            print(f"Mission accomplished, you neutralized the aerial threat!")
            airspace[next_row][next_col] = "J"
            break
        else:
            armor -= 100
            if armor <= 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
                airspace[next_row][next_col] = "J"
                break
            else:
                airspace[next_row][next_col] = "-"

    elif symbol == "R":
        armor = 300
        airspace[current_row][current_col] = "-"
        airspace[next_row][next_col] = "-"

    jet_pos = next_row, next_col


for row in airspace:
    print(f"{''.join(row)}")