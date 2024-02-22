from collections import deque


ramen = deque(map(int, input().split(', ')))
customers = deque(map(int, input().split(', ')))


while customers and ramen:
    current_ramen = ramen.pop()
    current_customer = customers.popleft()

    if current_customer == current_ramen:
        continue
    elif current_ramen > current_customer:
        ramen.append(current_ramen - current_customer)
    elif current_customer > current_ramen:
        customers.appendleft(current_customer - current_ramen)


if not customers:
    print("Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join(map(str, ramen))}")
else:
    if not ramen:
        print("Out of ramen! You didn't manage to serve all customers.")
        print(f"Customers left: {', '.join(map(str, customers))}")
