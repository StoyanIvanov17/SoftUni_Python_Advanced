from collections import deque

monster_armor = deque(map(int, input().split(',')))
soldier_striking = deque(map(int, input().split(',')))

defeated_monsters = 0

while monster_armor and soldier_striking:
    current_armor = monster_armor.popleft()
    current_strike = soldier_striking.pop()

    if current_strike >= current_armor:
        defeated_monsters += 1
        current_strike -= current_armor
        if soldier_striking:
            soldier_striking[-1] += current_strike
        elif not soldier_striking and current_strike > 0:
            soldier_striking.append(current_strike)

    else:
        monster_armor.append(current_armor - current_strike)

if not monster_armor:
    print("All monsters have been killed!")
if not soldier_striking:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {defeated_monsters}")