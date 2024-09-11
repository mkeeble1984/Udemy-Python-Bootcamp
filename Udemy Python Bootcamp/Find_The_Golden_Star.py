import random
import os
import time


def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item)
          for item in row]) for row in p_map]))


# Repeat the game until they choose not to play again.
play_again = True
while play_again is True:
    map1 = [["⬜️", "️⬜️", "️⬜️"], ["⬜️", "️⬜️", "️⬜️"], ["⬜️", "️⬜️", "️⬜️"]]
    print("This is our initial map...")
    rand_row = random.randint(0, 2)
    rand_col = random.randint(0, 2)
    guess_again = True
    while guess_again is True:  # Repeat until they choose not to guess again.
        print("A GOLDEN STAR is hidden somewhere in the map. Where do you think it is?\n")
        print_map(map1)
        user_row = input("\nWhat row is the star on? (1-3, X to quit) ")
        if user_row == "X" or user_row == "x":
            guess_again = False
            continue
        user_col = input("What column is the star on? (1-3, X to quit) ")

        user_row = int(user_row) - 1
        user_col = int(user_col) - 1
        if user_row == rand_row and user_col == rand_col:
            os.system("cls")
            print("Congratulations!!! You have found the Golden STAR!\n")
            map1[rand_row][rand_col] = "⭐"
            print_map(map1)
            guess_again = False

        else:
            print("\nUnfortunatly you didn't find it 🙁")
            time.sleep(2.5)
            map1[user_row][user_col] = "💩"
            os.system("cls")
            # print_map(map1)

    correct = False
    while correct is False:
        repeat = input("\nWould you like to play again? (Y / N)\n").upper()
        if repeat[0] == "Y":
            os.system("cls")
            break
        elif repeat[0] == "N":
            correct = True
            play_again = False
        else:
            print("You need to type either Yes or No. Please try again.")
