def cookbook(*args):
    origin_dic = {}
    meal_dic = {}

    for item in args:
        recipe_name = item[0]
        cuisine = item[1]
        ingredients = item[2]

        if cuisine not in origin_dic:
            origin_dic[cuisine] = []
        origin_dic[cuisine].append(recipe_name)

        meal_dic[recipe_name] = ingredients

    result = ''
    sorted_origin = sorted(origin_dic.items(), key=lambda x: (-len(x[1]), x[0]))
    for key, value in sorted_origin:
        sorted_values = sorted(value)
        result += f"{key} cuisine contains {len(value)} recipes:\n"

        for i in range(len(sorted_values)):
            current_cuisine = sorted_values[i]
            result += f"  * {current_cuisine} -> Ingredients: "
            current_ingredients = f"{', '.join(meal_dic[current_cuisine])}\n"
            result += current_ingredients

    return result.strip()
