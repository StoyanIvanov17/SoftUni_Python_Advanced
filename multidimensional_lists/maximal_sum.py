row, col = [int(x) for x in input().split()]

matrix = []

max_sum = float('-inf')
sub_matrix = []
total_sum = 0

for _ in range(row):
    matrix.append([int(el) for el in input().split()])

for row_index in range(row - 2):
    for col_index in range(col - 2):
        first_row = matrix[row_index][col_index:col_index + 3]
        second_row = matrix[row_index + 1][col_index:col_index + 3]
        third_row = matrix[row_index + 2][col_index:col_index + 3]

        total_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if max_sum < total_sum:
            max_sum = total_sum
            sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
print(*sub_matrix[0])
print(*sub_matrix[1])
print(*sub_matrix[2])
