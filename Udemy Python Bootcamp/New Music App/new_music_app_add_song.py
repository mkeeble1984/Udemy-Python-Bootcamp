"""Function to add a song to the playlist"""

import os
from new_music_app_playlist import playlist
from new_music_app_logo import LOGO


def add_song():
    """Function to add a song to the playlist"""
    os.system('cls')
    print(LOGO)

    add_artist = input(
        "\nWhat is the name of the artist you would like to add? ").capitalize

    if playlist.get(add_artist):
        print("Artist already exists.")
    else:
        print("Add artist to playlist.")


add_song()
