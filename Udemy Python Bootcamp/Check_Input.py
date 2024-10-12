"""Function to check if the user has enetered a number, not a word"""


def checkNumber(userInput, input_correct):
    try:
        userInput = int(userInput)
    except ValueError:
        print("You have not enetered a number.")
        input_correct = False
        return userInput, input_correct
    else:
        userInput = int(userInput)
        input_correct = True
        return userInput, input_correct
