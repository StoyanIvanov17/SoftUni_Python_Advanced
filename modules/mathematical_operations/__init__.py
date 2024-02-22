def operations(n1, operator, n2):
    if operator not in possible_operations:
        raise f"Operator {operator} not allowed. Allowed operators are '{', '.join(possible_operations)}'"

    if operator == "^":
        operator = "**"
    result = eval(f"{first_number} {operator} {second_number}")
    return f"{result:.2f}"


data = input().split()
first_number, operator, second_number = float(data[0]), data[1], int(data[2])

possible_operations = ["/", "*", "-", "+", "^"]

print(operations(first_number, operator, second_number))