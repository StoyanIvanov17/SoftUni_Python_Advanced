from collections import deque

elves = deque(map(int, input().split()))
boxes = deque(map(int, input().split()))

energy_used = 0
toys_count = 0
boxes_count = 0

while elves and boxes:
    elf_energy = elves.popleft()

    if elf_energy < 5:
        continue

    box = boxes.pop()
    energy = box
    boxes_count += 1
    toys_crafted = 1

    if boxes_count % 3 == 0:
        toys_crafted = 2
        energy *= 2

    if elf_energy >= energy:
        energy_used += energy

        if boxes_count % 5 != 0:
            toys_count += toys_crafted
            elves.append((elf_energy - energy) + 1)
        else:
            elves.append(elf_energy - energy)
    else:
        boxes.append(box)
        elves.append(elf_energy * 2)

print(f"Toys: {toys_count}")
print(f"Energy: {energy_used}")

if elves:
    print(f"Elves left: {', '.join(map(str, elves))}")
if boxes:
    print(f"Boxes left: {', '.join(map(str, boxes))}")
