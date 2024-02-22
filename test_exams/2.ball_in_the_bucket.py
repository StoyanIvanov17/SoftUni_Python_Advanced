size = 6
board = [input().split() for _ in range(size)]

scored_points = 0
prize_won = ''


for throws in range(3):
    coordinates = input().strip("(").strip(")").split(", ")
    row, col = [int(x) for x in coordinates]

    if not ( 0 <= row < size and 0 <= col < size):
        continue

    if board[row][col] == "B":
        for row in range(size):
            if board[row][col] != "B":
                scored_points += int(board[row][col])
        board[row][col] = 0


if 100 <= scored_points <= 199:
    prize_won = 'Football'
elif 200 <= scored_points <= 299:
    prize_won = "Teddy Bear"
elif scored_points >= 300:
    prize_won = "Lego Construction Set"


if prize_won:
    print(f"Good job! You scored {scored_points} points, and you've won {prize_won}.")
else:
    print(f"Sorry! You need {100 - scored_points} points more to win a prize.")