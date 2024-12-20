"""Function to add a song to the playlist"""

import os
import time
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

    if add_artist in playlist:  # If the artist is already in the playlist...
        os.system('cls')
        print(LOGO)
        print(f"\nHere are the albums for {add_artist}\n")

        temp_artist = playlist[add_artist]

        for num, key in enumerate(playlist[add_artist], 1):
            print(f"{num} - {key}")

        num = len(playlist[add_artist])
        print(f"\n{num} - Add a new album")

        choice = int(
            input(f"\nChoose an album to add to, or {num} to add a new album: "))

        if choice == num+1:  # Add a new album
            os.system('cls')
            print(LOGO)

            print(f"\nAdd a new album for {add_artist}")
            add_album = input("\nEnter the name of the album: ")
            add_album = string.capwords(add_album)

            add_track = input("\nEnter the name of the song: ")
            add_track = string.capwords(add_track)

            playlist[add_artist].update({add_album: {"Songs": [add_track]}})

        else:  # Add a new song to existing album
            os.system('cls')
            print(LOGO)

            add_album = list(temp_artist.values())[choice-1]

            print(
                f"\nAdd a new song to {add_artist} - {list(temp_artist.keys())[choice-1]}")

            add_track = input(
                "\nEnter the name of the song you would like to add: ")
            add_track = string.capwords(add_track)

            add_album['Songs'].append(add_track)

        print(
            f"\nTrack Added -\tARTIST - {add_artist}\n\t\tALBUM  - {list(temp_artist.keys())[choice-1]}\n\t\tSONG   - {add_track}")
        time.sleep(3)

    else:  # Add a new album to a new artist
        add_album = input("\nEnter the name of the album: ")
        add_album = string.capwords(add_album)

        add_track = input("\nEnter the name of the song: ")
        add_track = string.capwords(add_track)

        playlist[add_artist] = {add_album: {"Songs": [add_track]}}

        print(
            f"\nTrack Added -\tARTIST - {add_artist}\n\t\tALBUM  - {add_album}\n\t\tSONG   - {add_track}")
        time.sleep(3)
