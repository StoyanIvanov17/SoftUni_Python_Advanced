def numbers_searching(*args):
    arguments = list(args)
    removed_duplicates = set(args)
    missing_number_list = list(removed_duplicates)
    missing_number = []
    duplicates = []
    current_missing_number = 0

    for i in range(len(missing_number_list) - 1):
        current_num = missing_number_list[i]
        next_num = missing_number_list[i + 1]

        if current_num + 1 == next_num:
            continue
        else:
            current_missing_number = current_num + 1

    missing_number.append(current_missing_number)

    for num in arguments:
        if arguments.count(num) > 1:
            if num not in duplicates:
                duplicates.append(num)

    missing_number.append(sorted(duplicates))
    return missing_number
