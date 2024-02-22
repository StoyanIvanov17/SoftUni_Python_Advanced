from collections import deque
chocolates = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while milkshakes != 5 and chocolates and milk:
    current_milk = milk.popleft()
    current_chocolate = chocolates.pop()

    if current_chocolate <= 0 and current_milk <= 0:
        continue
    elif current_chocolate <= 0:
        milk.appendleft(current_milk)
        continue
    elif current_milk <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_milk:
        milkshakes += 1
    else:
        milk.append(current_milk)
        chocolates.append(current_chocolate - 5)

if milkshakes == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in milk) or 'empty'}")
