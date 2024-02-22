first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

functions = {
    'Add First': lambda x: [first_set.add(int(el)) for el in x],
    'Add Second': lambda x: [second_set.add(int(el)) for el in x],
    'Remove First': lambda x: [first_set.discard(int(el)) for el in x],
    'Remove Second': lambda x: [second_set.discard(int(el)) for el in x],
    'Check Subset': lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
}

for _ in range(int(input())):
    command_one, command_two, *data = input().split()

    final_command = command_one + ' ' + command_two

    functions[final_command](data)

print(*sorted(first_set), sep=', ')
print(*sorted(second_set), sep=', ')
