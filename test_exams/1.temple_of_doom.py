from collections import deque

tools = deque(map(int, input().split()))
substances = deque(map(int, input().split()))
challenges = deque(map(int, input().split()))

while tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    result = current_tool * current_substance

    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(current_tool + 1)
        if not current_substance - 1 == 0:
            substances.append(current_substance - 1)

if not tools or not substances:
    if challenges:
        print('Harry is lost in the temple. Oblivion awaits him.')
    else:
        print('Harry found an ostracon, which is dated to the 6th century BCE.')

if tools:
    print(f"Tools: {', '.join(map(str, tools))}")
if substances:
    print(f"Substances: {', '.join(map(str, substances))}")
if challenges:
    print(f"Challenges: {', '.join(map(str, challenges))}")