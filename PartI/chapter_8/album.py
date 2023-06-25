def make_album(artist_name, album_title, song_number=None):
    """Returns artist and ablum title"""
    album = {'name': artist_name, 'title': album_title,}
    if song_number:
        album['number'] = song_number
    return album

albums = make_album('eminem', 'recovery', 45)
print(albums)

albums = make_album('juice wrld', 'death race for love')
print(albums)

albums = make_album('drake', 'for your eyes only')
print(albums)
