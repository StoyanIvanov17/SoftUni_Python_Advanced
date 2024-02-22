from collections import deque
from math import floor

expression = deque(input().split())
current_index = 0

while current_index < len(expression):
    element = expression[current_index]

    if element == '*':
        for _ in range(current_index - 1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif element == '/':
        for _ in range(current_index - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
    elif element == '-':
        for _ in range(current_index - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif element == '+':
        for _ in range(current_index - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))

    if element in '*/+-':
        del expression[1]
        current_index = 1

    current_index += 1

print(floor(int(expression[0])))
