"""Main program for Music App."""

import os
from new_music_app_logo import LOGO
from new_music_app_random_song_function import choose_random
from new_music_app_choose_song_function import choose_song
from new_music_app_add_song import add_song

CHOICE = 0
while CHOICE != 4:
    os.system('cls')
    print(LOGO)

    print("\nWELCOME!\n\nWhat would you like to do today?")
    print("1. Choose a song.")
    print("2. Play a song at random.")
    print("3. Add a song.")
    print("4. Exit the app.")
    CHOICE = int(input("\nEnter your choice: "))

    if CHOICE == 1:
        choose_song()
    elif CHOICE == 2:
        choose_random()
    elif CHOICE == 3:
        add_song()

os.system('cls')
print(LOGO)
print("\nThanks - Come back soon!!")
