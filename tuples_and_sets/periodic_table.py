periodic_table = set()

for _ in range(int(input())):
    chemical_components = input().split()

    for component in chemical_components:
        periodic_table.add(component)

print(*periodic_table, sep='\n')