from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if food >= order:
        food -= order
        orders.popleft()
    else:
        print(f"Orders left:", *orders)
        break

if len(orders) <= 0:
    print('Orders complete')
