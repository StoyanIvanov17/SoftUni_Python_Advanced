from collections import deque

eggs = deque(map(int, input().split(', ')))
paper = deque(map(int, input().split(', ')))

boxes = 0

while eggs and paper:
    current_egg = eggs.popleft()
    current_paper = paper.pop()

    if current_egg == 13:
        first_to_last = paper.popleft()
        paper.appendleft(current_paper)
        paper.append(first_to_last)
        continue

    if current_egg <= 0:
        paper.append(current_paper)
        continue

    if current_egg + current_paper <= 50:
        boxes += 1
    else:
        continue

print(f"Great! You filled {boxes} boxes." if boxes > 0 else "Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if paper:
    print(f"Pieces of paper left: {', '.join(map(str, paper))}")