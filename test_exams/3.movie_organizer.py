def movie_organizer(*movies):
    collection = {}

    for movie, genre in movies:
        if genre not in collection:
            collection[genre] = []
        collection[genre].append(movie)

    sorted_collection = sorted(collection.items(), key=lambda x: (-len(x[1]), x[0]))

    result = ''
    for gen, mov in sorted_collection:
        sorted_movies = sorted(mov)
        result += f"{gen} - {len(mov)}\n"
        for m in sorted_movies:
            result += f"* {m}\n"

    return result
