from collections import deque

jobs = [int(x) for x in input().split(', ')]
number_at_index = int(input())

our_number = jobs.pop(number_at_index)
jobs.insert(number_at_index, "X")
clock_cycles = our_number
jobs = deque(jobs)

while jobs:
    job = jobs.popleft()

    if job == "X":
        continue

    elif job < our_number:
        clock_cycles += job

    elif job == our_number and "X" in jobs:
        clock_cycles += job

print(clock_cycles)