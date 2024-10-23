"""Main program for the Quiz App"""
import os
import time
from quiz_app_logo import quiz_app_logo
from quiz_app_questions import questions
from quiz_app_change_player import change_player

quiz_app_logo()

print("There are 6 questions, you can skip a question anytime by typing 'skip'.")
input("Press enter key to get started...")
print("\nThis is a 2 player game.")
player_one_name = input("Enter Player 1 name: ").capitalize()
player_two_name = input("Enter player 2 name: ").capitalize()
current_player = player_one_name
PLAYER_ONE_SCORE = 0
PLAYER_TWO_SCORE = 0
os.system('cls')

Q_NUM = 1
while Q_NUM < 7:
    quiz_app_logo()
    print(f"\n{player_one_name}'s score: {PLAYER_ONE_SCORE}")
    print(f"{player_two_name}'s score: {PLAYER_TWO_SCORE}")
    print(f"\nIt's {current_player}'s turn.\n")

    ATTEMPT = 0
    while ATTEMPT < 2:
        for key, value in questions[Q_NUM].items():
            print(f"Question: {key}")
            answer = input(
                "Answer ('skip' to move on to the next question): ").title()
            if answer == "Skip":
                Q_NUM += 1
                ATTEMPT = 3
                current_player = change_player(
                    player_one_name, player_two_name, current_player)
                os.system('cls')
                continue
            elif answer == value:
                print("\nCorrect!!!")
                time.sleep(3)
                if current_player == player_one_name:
                    PLAYER_ONE_SCORE += 1
                PLAYER_TWO_SCORE += 1
                Q_NUM += 1
                ATTEMPT = 3
                os.system('cls')
                current_player = change_player(
                    player_one_name, player_two_name, current_player)
                continue
            ATTEMPT += 1
            if ATTEMPT == 2:
                Q_NUM += 1
                print("\nIncorrect - Next question.")
                time.sleep(3)
                os.system('cls')
                current_player = change_player(
                    player_one_name, player_two_name, current_player)
            print("\nIncorrect - Try again.\n")

print("That is the end of the questions!\n")
print(f"{player_one_name}'s score: {PLAYER_ONE_SCORE}")
print(f"{player_two_name}'s score: {PLAYER_TWO_SCORE}")
if PLAYER_ONE_SCORE > PLAYER_TWO_SCORE:
    print(f"\n{player_one_name} is the winner!!!!!!")
elif PLAYER_ONE_SCORE < PLAYER_TWO_SCORE:
    print(f"\n{player_two_name} is the winner!!!!!!")
else:
    print("It's a draw!!!!!")

CORRECT = False
while CORRECT is False:
    choice = input(
        "\nWould you like to know the correct answers? (Y/N): ").upper()
    if choice == "Y":
        print()
        for q_num, qs in questions.items():
            for question, answer in qs.items():
                print(f"Question: {question}\nAnswer: {answer}")
        CORRECT = True
    elif choice == "N":
        print("\nThanks, play again soon!")
        time.sleep(3)
        CORRECT = True
    print("Invalid choice. Try again.")

print("\nThanks, play again soon!")
time.sleep(3)
