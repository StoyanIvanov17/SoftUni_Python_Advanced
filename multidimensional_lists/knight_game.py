board_size = int(input())
matrix = [list(input())for _ in range(board_size)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (1, 2),
)

removed_knights = 0

while True:
    max_attacks = 0
    greatest_attacking_knight = []

    for row in range(board_size):
        for col in range(board_size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < board_size and 0 <= pos_col < board_size:
                        if matrix[pos_row][pos_col] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    greatest_attacking_knight = [row, col]
                    max_attacks = attacks

    if greatest_attacking_knight:
        r, c = greatest_attacking_knight
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)