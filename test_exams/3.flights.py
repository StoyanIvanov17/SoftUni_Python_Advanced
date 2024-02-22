def flights(*args):
    flights_schedule = {}

    for i in range(0, len(args), 2):
        destination = args[i]

        if destination == "Finish":
            break

        passengers = int(args[i + 1])

        if destination not in flights_schedule:
            flights_schedule[destination] = 0
        flights_schedule[destination] += passengers

    return flights_schedule
