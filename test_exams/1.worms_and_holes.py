from collections import deque

worms = deque([int(x) for x in input().split()])
holes = deque([int(x) for x in input().split()])

matches = 0
number_of_worms = len(worms)

while worms and holes:
    current_worm = worms[-1]
    current_hole = holes.popleft()

    if current_worm == current_hole:
        worms.pop()
        matches += 1
    else:
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()


print(f"Matches: {matches}" if matches != 0 else "There are no matches.")

if matches != number_of_worms:
    print(f"Worms left: {', '.join(map(str, worms))}" if worms else "Worms left: none")
else:
    print("Every worm found a suitable hole!")

print(f"Holes left: {', '.join(map(str, holes))}" if holes else "Holes left: none")