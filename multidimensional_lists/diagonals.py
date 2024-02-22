rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

primary_diagonal = []
secondary_diagonal = []
for row_index in range(rows):
    primary_diagonal.append(matrix[row_index][row_index])
    secondary_diagonal.append(matrix[row_index][rows - row_index - 1])

print(f"Primary diagonal: {', '.join(str(el) for el in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")