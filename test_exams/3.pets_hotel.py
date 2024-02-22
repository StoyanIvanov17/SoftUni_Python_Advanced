def accommodate_new_pets(capacity, weight, *args):
    accommodated_pets = {}
    result = []
    pets_happy = True

    for pet_type, pet_weight in args:
        if capacity <= 0:
            result.append("You did not manage to accommodate all pets!\nAccommodated pets:")
            pets_happy = False
            break
        if pet_weight > weight:
            continue
        if pet_type not in accommodated_pets:
            accommodated_pets[pet_type] = 0
        accommodated_pets[pet_type] += 1
        capacity -= 1

    if pets_happy:
        result.append(f"All pets are accommodated! Available capacity: {capacity}.\nAccommodated pets:")

    [result.append(f"{pet}: {pet_count}") for pet, pet_count in sorted(accommodated_pets.items())]
    return '\n'.join(result)


print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
