def team_lineup(*args):
    storage = {}

    for arg in args:
        player, country = arg

        if country not in storage:
            storage[country] = []
        storage[country].append(player)

    sorted_storage = dict(sorted(storage.items(), key=lambda x: (-len(x[1]), x[0])))

    result = ''

    for each_country, each_player in sorted_storage.items():
        result += f"{each_country}:\n"

        for person in each_player:
            result += f"  -{person}\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
