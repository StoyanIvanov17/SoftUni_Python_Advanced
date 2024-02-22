from collections import deque

pizza_orders = deque(map(int, input().split(', ')))
employees = deque(map(int, input().split(', ')))

total_pizzas = 0

while pizza_orders and employees:
    current_order = pizza_orders.popleft()
    if current_order <= 0 or current_order > 10:
        continue

    current_employee = employees.pop()

    if current_order <= current_employee:
        total_pizzas += current_order

    else:
        while True:
            total_pizzas += current_employee
            current_order -= current_employee
            if not employees:
                pizza_orders.appendleft(current_order)
                break
            current_employee = employees.pop()

            if current_employee >= current_order:
                total_pizzas += current_order
                break

if not pizza_orders:
    print(f'All orders are successfully completed!\nTotal pizzas made: {total_pizzas}')
    print(f"Employees: {', '.join(map(str, employees))}")
elif pizza_orders and not employees:
    print(f"Not all orders are completed.\nOrders left: {', '.join(map(str, pizza_orders))}")

