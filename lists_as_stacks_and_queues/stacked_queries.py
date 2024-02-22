n = int(input())
stack = []
for i in range(n):
    command = [int(x) for x in input().split()]

    if command[0] == 1:
        stack.append(int(command[1]))

    elif command[0] == 2 and len(stack) > 0:
        stack.remove(max(stack))

    elif command[0] == 3 and len(stack) > 0:
        print(max(stack))

    elif command[0] == 4 and len(stack) > 0:
        print(min(stack))

stack.reverse()
print(*stack, sep=', ')
