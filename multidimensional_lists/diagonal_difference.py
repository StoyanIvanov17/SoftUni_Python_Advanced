rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

primary_sum, secondary_sum = 0, 0
for row_index in range(rows):
    primary_sum += matrix[row_index][row_index]
    secondary_sum += matrix[row_index][rows - row_index - 1]

print(abs(primary_sum - secondary_sum))