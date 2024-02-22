even_set = set()
odd_set = set()
counter = 1

for row in range(1, int(input()) + 1):
    ascii_name_sum = sum(ord(letter) for letter in input()) // row

    if ascii_name_sum % 2 == 0:
        even_set.add(ascii_name_sum)
    else:
        odd_set.add(ascii_name_sum)

odd_set_sum, even_set_sum = sum(odd_set), sum(even_set)

if even_set_sum == odd_set_sum:
    print(*odd_set.union(even_set), sep=', ')
elif even_set_sum < odd_set_sum:
    print(*odd_set.difference(even_set), sep=', ')
else:
    print(*odd_set.symmetric_difference(even_set), sep=', ')
    