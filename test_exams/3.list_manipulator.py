def list_manipulator(numbers, *args):
    command = args[0]
    place = args[1]
    values = [int(x) for x in args[2:]]

    if command == "add":
        if place == "beginning":
            values.extend(numbers)
            numbers = values
        else:
            numbers.extend(values)

    elif command == "remove":
        if place == "beginning":
            if values:
                for i in range(values[0]):
                    numbers.pop(0)
            if not values:
                numbers.pop(0)

        else:
            if values:
                for i in range(values[0]):
                    numbers.pop()
            if not values:
                numbers.pop()

    return numbers
