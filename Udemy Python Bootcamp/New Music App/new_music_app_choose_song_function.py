"""Function to allow user to choose the song they want to play"""

import os
import time
from new_music_app_logo import LOGO
from new_music_app_playlist import playlist
from new_music_app_selection_function import selection


def choose_song():
    """Function to allow user to choose the song they want to play"""

    os.system('cls')
    print(LOGO)
    print("\nARTISTS:")
    temp_artist, temp_dict, choice = selection("ARTISTS", playlist)

    print("\nALBUMS")
    temp_album, temp_dict, choice = selection("ALBUMS", temp_dict)

    print("\nSONGS")

    for value in temp_dict.values():
        for num, song in enumerate(value, 1):
            print(f"{num} - {song}")

    choice = int(input(
        "\nWhich song would you like to listen to today? (ENTER SONG NUMBER): "))

    temp_dict = temp_dict["Songs"]
    temp_song = temp_dict[choice-1]

    dots = ' ♫ '
    for _ in range(10):
        os.system('cls')
        print(LOGO)

        print(
            f"\nNow playing -\tARTIST - {temp_artist}\n\t\tALBUM  - {temp_album}\n\t\tSONG   - {temp_song} {dots}")
        dots = dots + ' ♫ '
        time.sleep(1)
