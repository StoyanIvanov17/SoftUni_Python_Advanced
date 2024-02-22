first_player, second_player = input().split(', ')
matrix = []

for _ in range(6):
    matrix.append(input().split())

first_player_rest = False
second_player_rest = False

while True:
    first_coordinates = input()
    if not first_player_rest:
        row, col = [int(x) for x in first_coordinates if x.isdigit()]
        if matrix[row][col] == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
        elif matrix[row][col] == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        elif matrix[row][col] == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            first_player_rest = True
    else:
        first_player_rest = False

    second_coordinates = input()
    if not second_player_rest:
        row, col = [int(x) for x in second_coordinates if x.isdigit()]
        if matrix[row][col] == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        elif matrix[row][col] == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        elif matrix[row][col] == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            second_player_rest = True
    else:
        second_player_rest = False
