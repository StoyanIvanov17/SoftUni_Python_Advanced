def forecast(*args):
    vacation_places = {"Sunny": [], "Cloudy": [], "Rainy": []}

    for place, weather in args:
        vacation_places[weather].append(place)

    result = ''
    for forecast, spot in vacation_places.items():
        for each_place in sorted(spot):
            result += f"{each_place} - {forecast}\n"

    return result
