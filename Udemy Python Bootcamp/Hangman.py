import os
import time
import Hangman_Image

new_game = True
while new_game:
    # STARTING SCREEN
    print("Welcome to HANGMAN!!!!\n")
    secret_word = input("Player 1 - Enter one word in secret:\n\n").upper()
    input("\nThank you - Press enter and pass to Player 2")
    guessed_letters = ""
    blank_secret = []
    lives = 6

    for _ in secret_word:
        blank_secret += "_"

    end_game = False
    while not end_game:
        os.system('cls')
        # MAIN PLAYER 2 SCREEN - RETURNED TO AFTER EACH ATTEMPT WITH UPDATED GUESSES
        str_blank_secret = " ".join(blank_secret)
        print(f"{str_blank_secret}\t\tLetters Already Guessed: {guessed_letters}")
        print(Hangman_Image.art(lives))
        guess = input("Player 2 - Guess a letter:\n\n").upper()

        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            time.sleep(2.5)

        else:
            guessed_letters = guessed_letters + guess + " "
            if guess in secret_word:
                # UPDATES GUESSED LETTERS STRING, ADDS CORRECT GUESS INTO SECRET WORD AND
                # CHECKS IF FULL WORD HAS BEEN GUESSED
                count = 0
                for _ in secret_word:
                    if guess == secret_word[count]:
                        blank_secret[count] = guess
                    count += 1
                if "_" not in blank_secret:
                    end_game = True
                    os.system("cls")
                    str_blank_secret = " ".join(blank_secret)
                    print(str_blank_secret)
                    print("\nWell done - You win!!!!!")
                    time.sleep(2.5)
                else:
                    print("Well done, you guessed one of the letters.")
                    time.sleep(2.5)

            else:
                # IF GUESS IS INCORRECT, PLAYER LOESES A LIFE UNTIL ALL LIVES LOST
                lives -= 1

                if lives == 0:
                    os.system("cls")
                    print(Hangman_Image.art(lives))
                    print("\nYou Lose!!!!!!")
                    print(f"\nThe word you wanted was: {secret_word}")
                    time.sleep(2.5)
                    end_game = True
                else:
                    print("Wrong! Try again.")
                    time.sleep(2.5)

    correct = False

    while not correct:
        os.system("cls")
        play_again = input("Would you like to play again?\n").upper()
        if play_again[0] == "Y":
            os.system("cls")
            correct = True
        elif play_again[0] == "N":
            os.system("cls")
            print("Thanks, that was fun. Play again soon I hope!!")
            time.sleep(2.5)
            correct = True
            new_game = False
        else:
            print("\nYou must enter either YES or NO.")
            time.sleep(2.5)
