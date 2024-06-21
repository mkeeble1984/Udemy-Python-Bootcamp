import os
from time import sleep


def checkNumber(score):  # Checks the input to be both a float and less than 1.0
    while True:
        try:
            score = float(score)
        except ValueError:
            print("\nYou have not enetered a number.")
            sleep(5)
            os.system('cls')
            score = input("Please enter a number: ")
        else:
            if score < 1:
                return score
            else:
                print("\nYou have not entered a score between 0.0 and 1.0.")
                sleep(5)
                os.system('cls')
                score = input("Enter a score: ")


print("Welcome to The Score Checker. Please enter a score between 0.0 and 1.0.")
# Pass user input into function, then convert to float if it passes
score = checkNumber(input("Enter Score: "))

# Check and output correct grade
if score >= 0.9:
    print(f"\nThe score: {score} is a grade A.")
elif score >= 0.8:
    print(f"\nThe score: {score} is a grade B.")
elif score >= 0.7:
    print(f"\nThe score: {score} is a grade C.")
elif score >= 0.6:
    print(f"\nThe score: {score} is a grade D.")
else:
    print(f"\nThe score: {score} is a grade F.")
