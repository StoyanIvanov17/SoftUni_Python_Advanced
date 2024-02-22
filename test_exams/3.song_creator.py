import os


def add_songs(*args):
    result = ""
    songs = {}

    for a in args:
        if a[0] not in songs:
            songs[a[0]] = []
        songs[a[0]].extend(a[1])
    result = []
    for title, lyrics in songs.items():
        result.append("- " + title)
        if lyrics:
            result.extend(lyrics)

    return os.linesep.join(result)
