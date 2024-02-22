def shopping_list(budget, **kwargs):
    basket = 0
    result = ''

    if budget < 100:
        return "You do not have enough budget."

    for product, info in kwargs.items():
        if basket == 5:
            break

        price, quantity = info
        if budget >= price * quantity:
            basket += 1
            budget -= price * quantity
            result += f"You bought {product} for {price * quantity:.2f} leva.\n"

    return result
