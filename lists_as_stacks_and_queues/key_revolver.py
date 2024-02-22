from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
value_intelligence = int(input())
shots = 0

bullets_copy = bullets.copy()
locks_copy = locks.copy()

while bullets_copy and locks_copy:
    if shots == gun_barrel_size:
        print('Reloading!')
        shots = 0
    if bullets_copy.pop() > locks_copy[0]:
        print('Ping!')
        shots += 1
    else:
        print('Bang!')
        locks_copy.popleft()
        shots += 1

if bullets_copy and shots == gun_barrel_size:
    print('Reloading!')
    shots = 0

if locks_copy:
    print(f"Couldn't get through. Locks left: {len(locks_copy)}")
else:
    bullets_cost = (len(bullets) - len(bullets_copy)) * bullet_price
    print(f'{len(bullets_copy)} bullets left. Earned ${value_intelligence - bullets_cost}')