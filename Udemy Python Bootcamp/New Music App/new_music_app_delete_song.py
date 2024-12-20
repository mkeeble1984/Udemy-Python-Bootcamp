"""Function to delete an artist, album or song"""

import os
from new_music_app_logo import LOGO
from new_music_app_playlist import playlist


def choose_artist():
    """Choose an artist to delete"""
    os.system('cls')
    print(LOGO)

    print("\nHere are the artists in the playlist\n")
    for num, key in enumerate(playlist, 1):
        print(f"{num} - {key}")

    choice = int(input("\nChoose an artist to delete: "))
    artist = list(playlist.keys())[choice-1]

    return artist


def choose_album(artist):
    """Choose an album to delete"""
    os.system('cls')
    print(LOGO)

    print(f"\nHere are the albums for {artist}\n")
    for num, key in enumerate(playlist[artist], 1):
        print(f"{num} - {key}")

    choice = int(input("\nChoose an album to delete: "))
    album = list(playlist[artist].keys())[choice-1]

    return album


def choose_song(artist, album):
    """Choose a song to delete"""
    os.system('cls')
    print(LOGO)

    print(f"\nHere are the songs in {artist} - {album}\n")
    for num, song in enumerate(playlist[artist][album]['Songs'], 1):
        print(f"{num} - {song}")

    choice = int(input("\nChoose a song to delete: "))
    song = playlist[artist][album]['Songs'][choice-1]

    return song


def delete_song():
    """Delete a song from the playlist"""
    os.system('cls')
    print(LOGO)

    print("\nWhat would you like to delete?")
    print("1. Artist")
    print("2. Album")
    print("3. Song")
    print("\n4. Return to main menu")
    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        artist = choose_artist()

        choice = input(f"\nAre you sure you want to delete {artist}? (y/n): ")
        if choice.lower() == 'y':
            del playlist[artist]

    elif choice == 2:
        artist = choose_artist()

        album = choose_album(artist)

        choice = input(f"\nAre you sure you want to delete {album}? (y/n): ")
        if choice.lower() == 'y':
            del playlist[artist][album]
    elif choice == 3:
        artist = choose_artist()

        album = choose_album(artist)

        song = choose_song(artist, album)

        choice = input(f"\nAre you sure you want to delete {song}? (y/n): ")
        if choice.lower() == 'y':
            playlist[artist][album]['Songs'].remove(song)
    elif choice == 4:
        return
    else:
        print("\nInvalid choice. Please try again.")
        os.system('pause')
        delete_song()

    os.system('pause')
    delete_song()


delete_song()
# Compare this snippet from Udemy%20Python%20Bootcamp/New%20Music%20App/new_music_app_playlist.py:
# """Playlist for the Music App"""
#
# playlist = {
#     "The Beatles": {
#         "Abbey Road": {
#             "Songs": ["Come Together", "Something", "Maxwell's Silver Hammer", "Oh! Darling", "Octopus's Garden", "I Want You (She's So Heavy)", "Here Comes the Sun", "Because", "You Never Give Me Your Money", "Sun King", "Mean Mr. Mustard", "Polythene Pam", "She Came in Through the Bathroom Window", "Golden Slumbers", "Carry That Weight", "The End", "Her Majesty"]
#         },
#         "Let It Be": {
#             "Songs": ["Two of Us", "Dig a Pony", "Across the Universe", "I Me Mine", "Dig It", "Let It Be", "Maggie Mae", "I've Got a Feeling", "One After 909", "The Long and Winding Road", "For You Blue", "Get Back"]
#         }
#     },
#     "The Rolling Stones": {
#         "Sticky Fingers": {
#             "Songs": ["Brown Sugar", "Sway", "Wild Horses", "Can't You Hear Me Knocking", "You Gotta
# Move", "

# Compare this snippet from Udemy%20Python%20Bootcamp/New%20Music%20App/new_music_app_random_song_function.py:
# """Function to choose a random song from the playlist"""
# import os
# import random
# import time
# from new_music_app_playlist import playlist
# from new_music_app_logo import LOGO
#
#
# def choose_random():
