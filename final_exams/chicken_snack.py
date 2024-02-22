from collections import deque

money = deque(map(int, input().split()))
prices = deque(map(int, input().split()))

foods_eaten = 0

while money and prices:
    change = 0
    current_money = money.pop()
    current_price = prices.popleft()

    if current_money == current_price:
        foods_eaten += 1

    elif current_money > current_price:
        foods_eaten += 1
        if money:
            change += current_money - current_price
            next_element = money.pop()
            next_element += change
            money.append(next_element)
        else:
            continue

    elif current_money < current_price:
        continue

if foods_eaten >= 4:
    print(f"Gluttony of the day! Henry ate {foods_eaten} foods.")

elif foods_eaten < 4 and foods_eaten > 1:
    print(f"Henry ate: {foods_eaten} foods.")

elif foods_eaten == 1:
    print(f"Henry ate: {foods_eaten} food.")

elif foods_eaten <= 0:
    print(f"Henry remained hungry. He will try next weekend again.")