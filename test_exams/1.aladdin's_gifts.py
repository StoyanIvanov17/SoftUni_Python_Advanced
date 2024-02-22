from collections import deque

materials = deque(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0


while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()
    total = magic + material

    if total < 100 and total % 2 == 0:
        material *= 2
        magic *= 3
        total = magic + material
    elif total < 100 and total % 2 != 0:
        material *= 2
        magic *= 2
        total = magic + material

    if total > 499:
        total /= 2

    if 100 <= total <= 199:
        gemstone += 1
    elif 200 <= total <= 299:
        porcelain_sculpture += 1
    elif 300 <= total <= 399:
        gold += 1
    elif 400 <= total <= 499:
        diamond_jewellery += 1

if gemstone and porcelain_sculpture or gold and diamond_jewellery:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

if diamond_jewellery > 0:
    print(f"Diamond Jewellery: {diamond_jewellery}")
if gemstone > 0:
    print(f'Gemstone: {gemstone}')
if gold > 0:
    print(f"Gold: {gold}")
if porcelain_sculpture > 0:
    print(f"Porcelain Sculpture: {porcelain_sculpture}")
