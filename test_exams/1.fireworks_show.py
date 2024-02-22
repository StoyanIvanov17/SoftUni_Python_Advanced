from collections import deque

fireworks = deque(map(int, input().split(', ')))
explosives = deque(map(int, input().split(', ')))


def show_validation():
    if crafted_fireworks["Palm Fireworks"] >= 3 \
            and crafted_fireworks["Willow Fireworks"] >= 3 \
            and crafted_fireworks["Crossette Fireworks"] >= 3:
        return True


crafted_fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

while fireworks and explosives:
    firework = fireworks.popleft()
    if firework <= 0:
        continue

    explosive = explosives.pop()
    if explosive <= 0:
        fireworks.appendleft(firework)
        continue

    total = firework + explosive

    if total % 3 == 0 and total % 5 != 0:
        crafted_fireworks["Palm Fireworks"] += 1

    elif total % 5 == 0 and total % 3 != 0:
        crafted_fireworks["Willow Fireworks"] += 1

    elif total % 5 == 0 and total % 3 == 0:
        crafted_fireworks["Crossette Fireworks"] += 1

    else:
        fireworks.append(firework - 1)
        explosives.append(explosive)

    if show_validation():
        print('Congrats! You made the perfect firework show!')
        break

if not show_validation():
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join(map(str, fireworks))}")
if explosives:
    print(f"Explosive Power left: {', '.join(map(str, explosives))}")

for key, value in crafted_fireworks.items():
    print(f"{key}: {value}")