def calculate_sum(row, col, size):
    total_sum = board[row][0] + board[row][size - 1] + board[0][col] + board[size - 1][col]
    return total_sum


size = 7
board = []

player_one, player_two = input().split(', ')

player_throws = {player_one: 0, player_two: 0}
player_points = {player_one: 501, player_two: 501}


for _ in range(size):
    current_row = [x if x.isalpha() else int(x) for x in input().split()]
    board.append(current_row)

turns = 0
while True:
    turns += 1
    if turns % 2 != 0:
        current_player = player_one
    else:
        current_player = player_two

    player_throws[current_player] += 1

    coordinates = input().strip("(").strip(")").split(", ")
    row, col = [int(x) for x in coordinates]

    if not (0 <= row < size and 0 <= col < size):
        continue

    target_hit = board[row][col]

    if str(target_hit).isnumeric():
        player_points[current_player] -= target_hit

    elif target_hit == "D":
        player_points[current_player] -= (calculate_sum(row, col, size) * 2)

    elif target_hit == "T":
        player_points[current_player] -= (calculate_sum(row, col, size) * 3)

    elif target_hit == "B":
        print(f"{current_player} won the game with {player_throws[current_player]} throws!")
        break

    if player_points[current_player] <= 0:
        print(f"{current_player} won the game with {player_throws[current_player]} throws!")
        break


