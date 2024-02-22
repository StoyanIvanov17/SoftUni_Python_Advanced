clothes = [int(x) for x in input().split()]
capacity = int(input())

number_racks = 1
rack_space_available = capacity

while clothes:
    piece_cloth = clothes.pop()

    if rack_space_available >= piece_cloth:
        rack_space_available -= piece_cloth
    else:
        number_racks += 1
        rack_space_available = capacity - piece_cloth

print(number_racks)