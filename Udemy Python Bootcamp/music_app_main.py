"""Main program for Music App."""

import os
import time
from music_app_tracks import playlist
from music_app_logo import LOGO

NEW_SONG = True
while NEW_SONG:

    os.system('cls')
    print(LOGO)
    print("\nARTISTS:")

    for b_index, band in enumerate(playlist, 1):
        name, songs = band
        print(f'\t{b_index} - {name}')

    artist_choice = int(input(
        "\nWho would you like to listen to today? (ENTER THE ARTISTS NUMBER): "))

    os.system('cls')
    print(LOGO)

    print(f'\n{playlist[artist_choice-1][0]}')
    for song_num, title in playlist[artist_choice-1][1]:
        print(f'\t{song_num} - {title}')

    track_choice = int(input(
        "\nWhat track would you like to listen to today? (ENTER THE TRACK NUMBER): "))

    DOTS = ' ♫ '
    for i in range(10):
        os.system('cls')
        print(LOGO)

        print(
            f'\nNow playing {playlist[artist_choice-1][0]} - {playlist[artist_choice-1][1][track_choice-1][1]}{DOTS}')
        DOTS = DOTS + ' ♫ '
        time.sleep(1)

    play_again = input(
        '\nWould you like to listen to something else? (Y/N): ').upper()

    if play_again == 'N':
        NEW_SONG = False
