from collections import deque

males = deque(map(int, input().split()))
females = deque(map(int, input().split()))

matches = 0

while males and females:
    current_male = males.pop()
    if current_male <= 0:
        continue

    if current_male % 25 == 0:
        males.pop()
        continue

    current_female = females.popleft()

    if current_female <= 0:
        males.append(current_male)
        continue

    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue

    if current_female == current_male:
        matches += 1
    else:
        males.append(current_male - 2)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join(map(str, reversed(males)))}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")
