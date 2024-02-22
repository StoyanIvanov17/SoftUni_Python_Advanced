rows, columns = [int(x) for x in input().split(',')]
cupboard = []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

command = ""
mouse_row, mouse_col = None, None
cheese = 0

for row in range(rows):
    cupboard.append(list(input()))

    if "M" in cupboard[row]:
        mouse_row, mouse_col = row, cupboard[row].index("M")
    if "C" in cupboard[row]:
        cheese += cupboard[row].count("C")


while cheese != 0:
    command = input()
    if command == 'danger':
        break

    next_row, next_col = mouse_row + directions[command][0], mouse_col + directions[command][1]

    if not (0 <= next_row < rows and 0 <= next_col < columns):
        print('No more cheese for tonight!')
        break

    if cupboard[next_row][next_col] == "@":
        continue
    if cupboard[next_row][next_col] == "T":
        cupboard[mouse_row][mouse_col] = "*"
        mouse_row, mouse_col = next_row, next_col
        cupboard[mouse_row][mouse_col] = "M"
        print('Mouse is trapped!')
        break
    if cupboard[next_row][next_col] == "*":
        cupboard[mouse_row][mouse_col] = "*"
        mouse_row, mouse_col = next_row, next_col
        cupboard[mouse_row][mouse_col] = "M"
        continue
    if cupboard[next_row][next_col] == "C":
        cheese -= 1
        cupboard[mouse_row][mouse_col] = "*"
        mouse_row, mouse_col = next_row, next_col
        cupboard[mouse_row][mouse_col] = "M"

else:
    print('Happy mouse! All the cheese is eaten, good night!')

if cheese and command == 'danger':
    print('Mouse will come back later!')

for rows in cupboard:
    print(f"{''.join(rows)}")