def make_album(artist_name, album_title, song_number=None):
    """Returns artist and ablum title"""
    album = {'name': artist_name, 'title': album_title,}
    if song_number:
        album['number'] = song_number
    return album

album = {}
while True:
    name = input("Artist Name:('q' to quit): ")
    if name == 'q':
        break

    title = input("Album Title:('q' to quit): ")
    if name == 'q':
        break

    album = make_album(name, title)

print(album)
