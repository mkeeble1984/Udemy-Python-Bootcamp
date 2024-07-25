import random
import Check_Input
import time
import os
import math

while True:
    lower = input("Enter a low number: ")
    lower = Check_Input.checkNumber(lower, "number")
    higher = input("Enter a high number: ")
    higher = Check_Input.checkNumber(higher, "number")

    if lower >= higher:
        print("The low number is not lower than the high number. Please try again.")
        time.sleep(3)
        os.system("cls")
        continue
    else:
        break

chances = int(math.log(higher - lower + 1, 2))
print(f"\n\tYou've only got {chances} chances to guess the number!\n")
random_number = random.randint(lower, higher)
num = 1
for num in range(1, chances + 1):
    guess = input(f"Guess a number between {lower} and {higher}: ")
    guess = Check_Input.checkNumber(guess, "number")
    if guess == random_number:
        raise SystemExit(
            f"Congratulation, you did it in {num} {'try' if num == 1 else 'tries'}.")
    elif guess > random_number:
        print("You guessed too high!")
    else:
        print("You guessed too low!")

print(
    f"The number you were trying to guess was {random_number}.  \n\tBetter luck next time!!!")
