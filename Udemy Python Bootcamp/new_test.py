"""Main program for Music App."""

import os
from matts_music_app_logo import LOGO
from matts_music_app_playlist import playlist
import time


def selection(user_dict):
    """function to display all keys within a dictionary, 
    allow a user to choose one then return the chosen dictionary."""
    count = 1
    for key in user_dict:
        print(f"\t{count} - {key}")
        count += 1

    choice = int(
        input("\nWhat would you like to listen to today? (ENTER THE NUMBER): "))

    user_choice = list(user_dict)[choice - 1]

    new_dict = user_dict[user_choice]

    return new_dict


os.system('cls')
print(LOGO)
print("\nARTISTS:")

selection(playlist)
