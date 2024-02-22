matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(matrix_size)]

while True:
    command = input().split()

    if command[0] == 'END':
        break

    action = command[0]
    row, col, value = [int(x) for x in command[1:]]

    if row in range(matrix_size) and col in range(matrix_size):
        if action == 'Add':
            if row in range(matrix_size) and col in range(matrix_size):
                matrix[row][col] += value
        elif action == 'Subtract':
            if row in range(matrix_size) and col in range(matrix_size):
                matrix[row][col] -= value
    else:
        print('Invalid coordinates')

[print(' '.join([str(x) for x in element])) for element in matrix]
