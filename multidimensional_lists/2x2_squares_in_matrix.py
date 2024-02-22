row, col = [int(x) for x in input().split()]

matrix = []

for _ in range(row):
    matrix.append([el for el in input().split()])

two_by_two_counter = 0

for row_index in range(row - 1):
    for col_index in range(col - 1):
        current_element = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]

        if current_element == next_element == element_below == element_diagonal:
            two_by_two_counter += 1

print(two_by_two_counter)