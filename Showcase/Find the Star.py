import random
import os
import time


def print_map(p_map):  # Function to print a 3 x 3 map
    print('\n'.join([' '.join(['{:2}'.format(item)
          for item in row]) for row in p_map]))


# Function to check if the user has enetered an integer, not a charachter
def checkNumber(userInput, var):
    try:
        userInput = int(userInput)
    except ValueError:
        print(f"\nYou have not enetered a {var}.")
        time.sleep(2.5)
        input_error = True
        return userInput, input_error
    else:
        userInput = int(userInput)
        input_error = False
        return userInput, input_error


# Function to check the user has entered correct values for either the row choice or column choice
def check_user_entry(row_or_col):
    input_error = True

    while input_error is True:
        user_input = input(
            f"\nWhat {row_or_col} is the star on? (1-3, X to quit) ").upper()

        if user_input == "X":
            input_error = False
            guess_again = False
        else:
            user_input, input_error = checkNumber(user_input, "number")

            if input_error is True:
                continue
            else:
                if 1 <= user_input <= 3:
                    input_error = False
                    guess_again = True
                else:
                    print("\nThe number must be between 1 and 3.")
                    time.sleep(2.5)
                    input_error = True

    return guess_again, user_input


# Start of the game
new_game = True
while new_game is True:
    # Initialise the map and generate a random location for the star
    map1 = [["⬜️", "️⬜️", "️⬜️"], ["⬜️", "️⬜️", "️⬜️"], ["⬜️", "️⬜️", "️⬜️"]]
    rand_row = random.randint(0, 2)
    rand_col = random.randint(0, 2)

    correct_guess = False
    guess_again = True
    while correct_guess is False and guess_again is True:
        # Take user guess and repeat as long as they choose too, or they guess correctly
        print("A GOLDEN STAR is hidden somewhere in the map. Where do you think it is?\n")
        print_map(map1)

        guess_again, user_input = check_user_entry("row")
        if user_input != "X":
            user_row = user_input

            guess_again, user_input = check_user_entry("column")
            if user_input != "X":
                user_col = user_input

                user_row = int(user_row) - 1
                user_col = int(user_col) - 1

                if user_row == rand_row and user_col == rand_col:
                    os.system("cls")
                    print(
                        "\033[5mCongratulations!!! You have found the Golden STAR!\033[0m\n")
                    map1[rand_row][rand_col] = "⭐"
                    print_map(map1)
                    guess_again = False

                else:
                    print("\nUnfortunatly you didn't find the hidden star 🙁")
                    time.sleep(2.5)
                    map1[user_row][user_col] = "💩"
                    os.system("cls")

    correct = False
    while correct is False:
        repeat = input(
            "\nWould you like to play again? (Y / N)\n").upper()
        if repeat[0] == "Y":
            os.system("cls")
            break
        elif repeat[0] == "N":
            correct = True
            new_game = False
        else:
            print("You need to type either Yes or No. Please try again.")

print("\nThanks, Maybe we can play again some other time.")
