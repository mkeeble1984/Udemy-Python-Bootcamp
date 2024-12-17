"""Function to add a song to the playlist"""

import os
import string
from new_music_app_playlist import playlist
from new_music_app_logo import LOGO


def add_song():
    """Function to add a song to the playlist"""
    os.system('cls')
    print(LOGO)

    add_artist = input(
        "\nEnter the name of the artist you would like to add: ")
    add_artist = string.capwords(add_artist)

    if add_artist in playlist:
        os.system('cls')
        print(LOGO)
        print(f"\nHere are the albums for {add_artist}\n")

        temp_artist = playlist[add_artist]

        for num, key in enumerate(playlist[add_artist], 1):
            print(f"{num} - {key}")

        choice = int(input("\nWhich ablum would you like to add to? "))

        add_album = list(temp_artist.values())[choice-1]

        add_track = input(
            "\nEnter the name of the song you would like to add: ")
        add_track = string.capwords(add_track)

        add_album['Songs'].append(add_track)

    else:
        add_album = input("\nEnter the name of the album: ")
        add_album = string.capwords(add_album)

        add_track = input("\nEnter the name of the song: ")
        add_track = string.capwords(add_track)

        playlist[add_artist] = {add_album: {"Songs": [add_track]}}


add_song()
