from collections import deque

textiles = deque(map(int, input().split()))
medicaments = deque(map(int, input().split()))

healing_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0
}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    result = current_textile + current_medicament

    if result == 30:
        healing_items["Patch"] += 1
    elif result == 40:
        healing_items["Bandage"] += 1
    elif result == 100:
        healing_items["MedKit"] += 1
    elif result > 100:
        healing_items["MedKit"] += 1
        medicaments[-1] += result - 100
    else:
        medicaments.append(current_medicament + 10)


if not textiles or not medicaments:
    if not textiles and not medicaments:
        print('Textiles and medicaments are both empty.')
    elif not textiles:
        print('Textiles are empty.')
    elif not medicaments:
        print('Medicaments are empty.')


sorted_items = sorted(healing_items.items(), key=lambda x: (-x[1], x[0]))
for item in sorted_items:
    if item[1] > 0:
        print(f"{item[0]} - {item[1]}")


if medicaments:
    medicaments.reverse()
    print(f"Medicaments left: {', '.join(map(str, medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")