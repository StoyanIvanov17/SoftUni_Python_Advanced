from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())

queue = deque()
cars_passed = 0
crash = False

while True:
    command = input()
    if command == 'END':
        break

    if command == 'green':
        if queue:
            current_car = queue.popleft()
            time_remaining = green_light_duration - len(current_car)
            while time_remaining > 0:
                cars_passed += 1
                if queue:
                    current_car = queue.popleft()
                    time_remaining -= len(current_car)
                else:
                    break
            if time_remaining == 0:
                cars_passed += 1
            if free_window_duration >= abs(time_remaining):
                if time_remaining < 0:
                    cars_passed += 1
            else:
                idx = free_window_duration + time_remaining
                print('A crash happened!')
                print(f"{current_car} was hit at {current_car[idx]}.")
                crash = True
                break

    else:
        queue.append(command)

if not crash:
    print('Everyone is safe.')
    print(f'{cars_passed} total cars passed the crossroads.')