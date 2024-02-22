def check_captured_pawns(attackers, defenders):
    attacker_row, attacker_col = attackers[0], attackers[1]
    defender_row, defender_col = defenders[0], defenders[1]

    if attacker_row - 1 == defender_row and attacker_col - 1 == defender_col:
        return [attacker_row - 1, attacker_col - 1]
    elif attacker_row - 1 == defender_row and attacker_col + 1 == defender_col:
        return [attacker_row - 1, attacker_col + 1]
    elif attacker_row + 1 == defender_row and attacker_col - 1 == defender_col:
        return [attacker_row + 1, attacker_col - 1]
    elif attacker_row + 1 == defender_row and attacker_col + 1 == defender_col:
        return [attacker_row + 1, attacker_col + 1]


matrix = []

white_pawn_coordinates = []
black_pawn_coordinates = []


for row in range(8):
    matrix.append(input().split())

    if "w" in matrix[row]:
        white_pawn_coordinates = [row, matrix[row].index("w")]
    if "b" in matrix[row]:
        black_pawn_coordinates = [row, matrix[row].index("b")]


position_row = {
    0: '8',
    1: '7',
    2: '6',
    3: '5',
    4: '4',
    5: '3',
    6: '2',
    7: '1',
}

position_col = {
    0: 'a',
    1: 'b',
    2: 'c',
    3: 'd',
    4: 'e',
    5: 'f',
    6: 'g',
    7: 'h'
}


for _ in range(8):
    position_on = check_captured_pawns(white_pawn_coordinates, black_pawn_coordinates)
    if position_on:
        position = position_col[position_on[1]] + position_row[position_on[0]]
        print(f"Game over! White win, capture on {position}.")
        break

    white_pawn_coordinates[0] -= 1

    if white_pawn_coordinates[0] == 0:
        position = position_col[white_pawn_coordinates[1]] + position_row[white_pawn_coordinates[0]]
        print(f"Game over! White pawn is promoted to a queen at {position}.")
        break

    position_on = check_captured_pawns(black_pawn_coordinates, white_pawn_coordinates)

    if position_on:
        position = position_col[position_on[1]] + position_row[position_on[0]]
        print(f"Game over! Black win, capture on {position}.")
        break

    black_pawn_coordinates[0] += 1

    if black_pawn_coordinates[0] == 7:
        position = position_col[black_pawn_coordinates[1]] + position_row[black_pawn_coordinates[0]]
        print(f"Game over! Black pawn is promoted to a queen at {position}.")
        break
