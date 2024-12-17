"""Function to select a song from the playlist at random"""

import random
import os
import time
from new_music_app_logo import LOGO
from new_music_app_playlist import playlist


def choose_random():
    """Function to select a song from the playlist at random"""

    temp_artist, temp_album = random.choice(list(playlist.items()))

    temp_album, temp_song = random.choice(list(temp_album.items()))

    temp_album2 = temp_song["Songs"]

    temp_song = random.choice(temp_album2)

    dots = ' ♫ '

    for _ in range(10):
        os.system('cls')
        print(LOGO)
        print(
            f"\nNow playing -\tARTIST - {temp_artist}\n\t\tALBUM  - {temp_album}\n\t\tSONG   - {temp_song} {dots}")
        dots = dots + ' ♫ '
        time.sleep(1)
