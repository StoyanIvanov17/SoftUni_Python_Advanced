def shopping_cart(*args):
    products_plan = {"Soup": [], "Pizza": [], "Dessert": []}

    for _tuple in args:
        if _tuple == "Stop":
            break
        product = _tuple[0]
        ingredient = _tuple[1]

        if product == "Soup" and len(products_plan["Soup"]) == 3:
            continue
        elif product == "Pizza" and len(products_plan["Pizza"]) == 4:
            continue
        elif product == "Dessert" and len(products_plan["Dessert"]) == 2:
            continue
        if ingredient not in products_plan[product]:
            products_plan[product].append(ingredient)

    for values in products_plan.values():
        if len(values) > 0:
            break
    else:
        return "No products in the cart!"

    result = ""
    sorted_products = dict(sorted(products_plan.items(), key=lambda x: (-len(x[1]), x[0])))

    for key, value in sorted_products.items():
        result += f"{key}:\n"
        sorted_values = sorted(value)
        for v in sorted_values:
            result += f" - {v}\n"

    return result
