def grocery_store(**kwargs):
    receipt = ''

    sorted_products = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for product, quantity in sorted_products:
        receipt += f"{product}: {quantity}\n"

    return receipt


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
