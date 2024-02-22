all_lists_together = [[x for x in first.split()] for first in input().split('|')]
flattened_list = []

while all_lists_together:
    current_list = all_lists_together.pop()
    flattened_list.extend(current_list)

print(*flattened_list)
