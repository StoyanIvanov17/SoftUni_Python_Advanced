from collections import deque


customers = deque(map(int, input().split(', ')))
taxis = deque(map(int, input().split(', ')))

total_time = 0

while customers and taxis:
    customer = customers[0]
    taxi = taxis.pop()

    if taxi >= customer:
        customers.popleft()
        total_time += customer


if not customers:
    print(f"All customers were driven to their destinations\nTotal time: {total_time} minutes")
elif not taxis and customers:
    print(f"Not all customers were driven to their destinations\nCustomers left: {', '.join(map(str, customers))}")
