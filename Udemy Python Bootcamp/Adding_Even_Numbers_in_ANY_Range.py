import Check_Input
import time
import os

check = False


# Enters the start and end number chosen by the user then adds every even number together, skipping over the odd numbers.
def add_even_numbers(start, end):
    total = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            total += number
    return total


# Checks to see if user has entered a number and not a letter, and that the starting number is less than the end number.
while check == False:
    start = input("Please enter a starting number: ")
    start = Check_Input.checkNumber(start, "number")

    end = input("Please enter an end number: ")
    end = Check_Input.checkNumber(end, "number")

    if start < end:
        check = True
    else:
        print("Your starting number must be less than your end number. Please try again.")
        time.sleep(3)
        os.system('cls')


print(
    f"The total of all the even numbers within your range is {add_even_numbers(start, end)}.")
