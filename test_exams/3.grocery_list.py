def shop_from_grocery_list(budget, grocery_list, *products):
    bought_products = []

    for product_name, price in products:
        if product_name not in grocery_list:
            continue
        if product_name in bought_products:
            continue
        if budget - float(price) < 0:
            break
        else:
            bought_products.append(product_name)
            budget -= float(price)
            grocery_list.remove(product_name)

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(map(str, grocery_list))}."
