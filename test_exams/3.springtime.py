def start_spring(**kwargs):
    flowers = {}

    for key, value in kwargs.items():
        flowers[value] = flowers.get(value, []) + [key]

    sorted_flowers = sorted(flowers.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''

    for item, item_type in sorted_flowers:
        result += f"{item}:\n"
        sorted_item_type = sorted(item_type)
        for flower in sorted_item_type:
            result += f"-{flower}\n"

    return result
