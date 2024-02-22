from collections import deque

seats = input().split(', ')
first_sequence = deque(map(int, input().split(', ')))
second_sequence = deque(map(int, input().split(', ')))

seat_matches = []
rotations = 0

while True:
    if len(seat_matches) == 3:
        break
    if rotations == 10:
        break

    num_one = first_sequence.popleft()
    num_two = second_sequence.pop()
    result = num_one + num_two
    ascii_result = chr(result)

    first_seat = str(num_one) + ascii_result
    second_seat = str(num_two) + ascii_result

    for seat in [first_seat, second_seat]:
        if seat in seat_matches:
            break
        if seat in seats:
            seat_matches.append(seat)
            seats.remove(seat)
    else:
        first_sequence.append(num_one)
        second_sequence.appendleft(num_two)

    rotations += 1


print(f"Seat matches: {', '.join(seat_matches)}")
print(f"Rotations count: {rotations}")