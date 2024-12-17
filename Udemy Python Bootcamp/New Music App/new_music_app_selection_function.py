"""function to allow user to view all kyes in 'Playlist' dictionary, then 'Artist' dictionary"""

import os
from new_music_app_logo import LOGO

### get song selection to display chosen song same as random song screen ###


def selection(option, dictionary):
    """function to display all keys within a dictionary,
    allow a user to choose one then return the chosen dictionary."""

    for num, key in enumerate(dictionary, 1):
        print(f"{num} - {key}")

    choice = int(input(
        f"\nWhat would you like to listen to today? (ENTER {option} NUMBER): "))
    return_key, return_value = list(dictionary.items())[choice - 1]

    os.system('cls')
    print(LOGO)

    print(f"\nYou have selected - {list(dictionary)[choice - 1]}.")

    return return_key, return_value, choice
