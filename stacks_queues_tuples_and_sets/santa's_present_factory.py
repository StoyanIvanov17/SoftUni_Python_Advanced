from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque(int(x) for x in input().split())

crafted_toys = []
presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

while materials and magic_values:
    current_box = materials.pop() if magic_values[0] or not materials[-1] else 0
    current_magic_level = magic_values.popleft() if current_box or not magic_values[0] else 0

    if not current_magic_level:
        continue

    product = current_box * current_magic_level

    if presents.get(product):
        crafted_toys.append(presents[product])
    elif product < 0:
        materials.append(current_box + current_magic_level)
    elif product > 0:
        materials.append(current_box + 15)

if {"Doll", "Wooden train"}.issubset(crafted_toys) or {"Teddy bear", "Bicycle"}.issubset(crafted_toys):
    print('The presents are crafted! Merry Christmas!')
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")

if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")

[print(f"{toy}: {crafted_toys.count(toy)}") for toy in sorted(set(crafted_toys))]
