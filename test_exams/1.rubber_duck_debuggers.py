from collections import deque

time = deque(map(int, input().split()))
task_number = deque(map(int, input().split()))

ducks_received = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while time and task_number:
    current_time = time.popleft()
    current_task = task_number.pop()
    result = current_time * current_task

    if 0 <= result <= 60:
        ducks_received["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        ducks_received["Thor Ducky"] += 1
    elif 121 <= result <= 180:
        ducks_received["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        ducks_received["Small Yellow Rubber Ducky"] += 1
    else:
        time.append(current_time)
        task_number.append(current_task - 2)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck, count in ducks_received.items():
    print(f"{duck}: {count}")