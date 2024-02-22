from collections import deque

caffeine_milligrams = deque(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))

caffeine_limit = 0

while caffeine_milligrams and energy_drinks:

    if caffeine_limit >= 300:
        break

    current_caffeine = caffeine_milligrams.pop()
    current_energy = energy_drinks.popleft()
    total = current_caffeine * current_energy

    if caffeine_limit + total <= 300:
        caffeine_limit += total
    else:
        energy_drinks.append(current_energy)
        caffeine_limit -= 30
        if caffeine_limit < 0:
            caffeine_limit = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {caffeine_limit} mg caffeine.")