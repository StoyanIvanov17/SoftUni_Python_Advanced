from collections import deque

altitudes_counter = deque(["Altitude 1", "Altitude 2", "Altitude 3", "Altitude 4"])

initial_fuel = deque([int(x) for x in input().split()])
consumption = deque([int(x) for x in input().split()])
needed_fuel = deque([int(x) for x in input().split()])


altitudes_info = {}
for altitude in altitudes_counter:
    altitudes_info[altitude] = needed_fuel.popleft()

reached_altitudes = []

while initial_fuel and consumption:
    current_altitude = altitudes_counter.popleft()
    spent_fuel = initial_fuel.pop() - consumption.popleft()

    if spent_fuel >= altitudes_info[current_altitude]:
        reached_altitudes.append(current_altitude)
        print(f"John has reached: {current_altitude}")
    else:
        print(f"John did not reach: {current_altitude}\nJohn failed to reach the top.")
        break

if not altitudes_info:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    if reached_altitudes:
        print(f"Reached altitudes: {', '.join(alt for alt in reached_altitudes)}")
    else:
        print("John didn't reach any altitude.")
